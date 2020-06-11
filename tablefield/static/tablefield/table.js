'use strict';
(function($){

function initTable(id, tableOptions) {
    var containerId = id + '-handsontable-container';
    var tableHeaderCheckboxId = id + '-handsontable-header';
    var colHeaderCheckboxId = id + '-handsontable-col-header';
    var hiddenStreamInput = $('#' + id);
    var tableHeaderCheckbox = $('#' + tableHeaderCheckboxId);
    var colHeaderCheckbox = $('#' + colHeaderCheckboxId);
    var hot;
    var defaultOptions;
    var finalOptions = {};
    var persist = function() {};
    var cellEvent;
    var cellsMeta = [];
    var structureEvent;
    var dataForForm = null;
    var getWidth = function() {
        return $('.widget-table_input').closest('.sequence-member-inner').width();
    };
    var getHeight = function() {
        var tableParent = $('#' + id).parent();
        return tableParent.find('.htCore').height() + (tableParent.find('.input').height() * 2);
    };
    var height = getHeight();
    var resizeTargets = ['.input > .handsontable', '.wtHider', '.wtHolder'];
    var resizeHeight = function(height) {
        var currTable = $('#' + id);
        $.each(resizeTargets, function() {
            currTable.closest('.field-content').find(this).height(height);
        });
    };
    function resizeWidth(width) {
        $.each(resizeTargets, function() {
            $(this).width(width);
        });
        var parentDiv = $('.widget-table_input').parent();
        parentDiv.find('.field-content').width(width);
        parentDiv.find('.fieldname-table .field-content .field-content').width('80%');
    }

    try {
        dataForForm = JSON.parse(hiddenStreamInput.val());
    } catch (e) {
        // do nothing
    }

    if (dataForForm !== null) {
        if (dataForForm.hasOwnProperty('first_row_is_table_header')) {
            tableHeaderCheckbox.prop('checked', dataForForm.first_row_is_table_header);
        }
        if (dataForForm.hasOwnProperty('first_col_is_header')) {
            colHeaderCheckbox.prop('checked', dataForForm.first_col_is_header);
        }
    }

    if (!tableOptions.hasOwnProperty('width') || !tableOptions.hasOwnProperty('height')) {
        // Size to parent .sequence-member-inner width if width is not given in tableOptions
        $(window).on('resize', function() {
            hot.updateSettings({
                width: getWidth(),
                height: getHeight()
            });
            resizeWidth('100%');
        });
    }

    cellEvent = function(change, source) {
        if (source === 'loadData') {
            return; //don't save this change
        }
        persist();
    };

    structureEvent = function(index, amount) {
        resizeHeight(getHeight());
        persist();
    };

    defaultOptions = {
        afterChange: cellEvent,
        afterCreateCol: structureEvent,
        afterCreateRow: structureEvent,
        afterRemoveCol: structureEvent,
        afterRemoveRow: structureEvent,
        afterUnmergeCells: structureEvent,
        afterSetCellMeta: function (row, col, key, val) {
            if (key != 'className') return;
            var existed = cellsMeta.find(function(x){
                return x.row == row && x.col == col && x.key == key;
            });
            if (existed) {
                existed.val = val;
            } else {
                cellsMeta.push({'row': row, 'col': col, 'key': key, 'val': val});
            }
            persist();
        }
    };

    if (dataForForm !== null) {
        // Overrides default value from tableOptions (if given) with value from database
        if (dataForForm.hasOwnProperty('data')) {
            defaultOptions.data = dataForForm.data;
        }
        if (dataForForm.hasOwnProperty('mergeCells')) {
            tableOptions['mergeCells'] = dataForForm.mergeCells;
        }
    }
    Object.keys(defaultOptions).forEach(function (key) {
        finalOptions[key] = defaultOptions[key];
    });
    Object.keys(tableOptions).forEach(function (key) {
        finalOptions[key] = tableOptions[key];
    });

    hot = new Handsontable(document.getElementById(containerId), finalOptions);

    // CellsMeta
    if (typeof dataForForm.cellsMeta !== 'undefined') {
        for (var i = dataForForm.cellsMeta.length - 1; i >= 0; i--) {
            var o = dataForForm.cellsMeta[i];
            hot.setCellMeta(o.row, o.col, o.key, o.val);
        }
    }

    persist = function() {
        hiddenStreamInput.val(JSON.stringify({
            data: hot.getData(),
            first_row_is_table_header: tableHeaderCheckbox.prop('checked'),
            first_col_is_header: colHeaderCheckbox.prop('checked'),
            mergeCells: hot.getPlugin('mergeCells').mergedCellsCollection.mergedCells,
            cellsMeta: cellsMeta
        }));
    };

    tableHeaderCheckbox.on('change', function() {
        persist();
    });

    colHeaderCheckbox.on('change', function() {
        persist();
    });

    hot.render(); // Call to render removes 'null' literals from empty cells

    // Apply resize after document is finished loading (parent .sequence-member-inner width is set)
    if ('resize' in $(window)) {
        resizeHeight(getHeight());
        $(window).on('load', function() {
            $(window).trigger('resize');
        });
    }
    window.hot = hot;
}
window.initTable = initTable;
})(django.jQuery)