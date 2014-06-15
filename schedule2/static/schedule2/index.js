$(document).ready(function() {
    var lastColumn = 8; // index of the last column
    var lastRow = 25; // index of the last row

    // initial settings for table creation
    var table = $('#schedule').DataTable( {
        "paging": false,
        "searching": false,
        "info": false,
        "ordering":false,
    } );

    // gets a CSRF token for csrf protection
    var csrftoken = $.cookie('csrftoken');

    // csrf setup
    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    // handles the initial parameters for ajax calls
    $.ajaxSetup({
        crossDomain: false,
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type)) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });
    
    //For multiselect checkbox list
    $('.dropdown-menu').on('click', function(event) {
        if($(this).hasClass('dropdown-menu-form')) {
            event.stopPropagation();
        }
    });

    // Checks for correct input on all forms
    function checkSubmission() {
        var name = document.getElementById('nameInput').value;
        
        if (name !== ""){
            return true
            }
        return false;
    }

    // Sends AJAX POST if all forms have acceptable submissions
    $('form').submit(function(event) {
        if (checkSubmission()) {
            // sends an AJAX  post request with data on cells selected
            // Name, Area, and Sub-Areas
            $.post("testPost/",
                {
                    name: document.getElementById('nameInput').value,
                    areas: document.getElementById('areaInput').value,
                    'cell row': 3,
                    'cell column': 5,
                },
                function(data, status) {
                    $(".alert").alert(data, status);
                });
        }
        event.preventDefault();
    });

    // adds select class to a cell
    function selectCell(cellObj) {
        if ( !$( table.cell(cellObj).node() ).hasClass( 'time' )) {
            $( table.cell(cellObj).node() ).addClass( 'select' );
        }
    }

    // removes select class from a cell
    function removeSelectCell(cellObj) {
        $( table.cell(cellObj).node() ).removeClass( 'select' );
    }

    // when a cell is clicked if it does not have select class calls 
    // selectCell()
    $('#schedule tbody').on( 'click', 'td', function() {
        if ( $( table.cell(this).node() ).hasClass( 'select' )) {
            removeSelectCell(this);
        } else {
            selectCell(this);
        }
    } );

    // adds select class to a row of cells
    function selectRowOfCells(rowId) {
        for (var i = 1; i < lastColumn; i++) {
            $( table.cells(rowId, i).nodes() ).addClass( 'select' );
        }
    }

    // removes select class from a row of cells
    function deselectRowOfCells(rowId) {
        for (var i = 1; i < lastColumn; i++) {
            $( table.cells(rowId, i).nodes() ).removeClass( 'select' );
        }
    }

    // selects a row of cells on click, deselects only if all cells in
    // row are already selected
    $('#schedule tbody').on( 'click', 'td.time', function() {
        var rowIdx = table.cell(this).index().row;
        var selected = true;

        for (var columnIndex = 1; columnIndex < lastColumn; columnIndex++) {
            var checkSelect = $( table.cells(rowIdx, columnIndex).nodes() )
                                      .hasClass( 'select' );

            if ( !checkSelect ) {
                selected = false;
            }
        }

        if ( selected ) {
            deselectRowOfCells(rowIdx);
        } else {
            selectRowOfCells(rowIdx);
        }
    });

    // adds select class to a Column of cells
    function selectColumnOfCells(colId) {
        $( table.column(colId).nodes() ).addClass( 'select' );
    }

    // removes select class from a row of cells
    function deselectColumnOfCells(colId) {
        $( table.column(colId).nodes() ).removeClass( 'select' );
    }

    // selects a column of cells on click, deselects only if all cells in
    // column are already selected.
    $('#schedule').on( 'click', 'td.days', function() {
        var colIdx = table.column(this).index();
        var selected = true;

        for (var rowIndex = 1; rowIndex < lastRow; rowIndex++) {
            var checkSelect = $( table.cells(rowIndex, colIdx).nodes() )
                                      .hasClass( 'select' );

            if ( !checkSelect ) {
                selected = false;
            }
        }

        if (selected) {
            deselectColumnOfCells(colIdx);
        } else {
            selectColumnOfCells(colIdx);
        }
    }); 


    // adds select class to all cells
    function selectAllCells() {
        for (var i = 1; i < lastColumn; i++) {
            $( table.column(i).nodes() ).addClass( 'select' );
        }
    }

    // removes select class from all cells
    function deselectAllCells() {
        for (var i = 1; i < lastColumn; i++) {
            $( table.column(i).nodes() ).removeClass( 'select' );
        }
    }

    // acts as the control for select all / deselect all
    var selAllSwitch = 0;

    // if td with class select-all is clicked, all cells are selected
    // except for those with time class. If clicked again, deselects all
    $('#schedule thead').on( 'click', 'td.select-all', function() {
        if (selAllSwitch == 0) {
            selectAllCells();
            selAllSwitch++;
        } else {
            deselectAllCells();
            selAllSwitch--;
        }
    } );

    // TODO: get row highlighting to work
    // handles the highlighting of columns and rows on mouseover
    $('#schedule tbody').on( 'mouseover', 'td', function() {
        var colIdx = table.cell(this).index().column;
        var rowIdx = table.cell(this).index().row;
        var lastIdx = null;

        if ( colIdx !== lastIdx && colIdx !== 0 && rowIdx !== lastIdx ) {
            $( table.cells().nodes() ).removeClass( 'highlight' );
            $( table.column( colIdx ).nodes() ).addClass( 'highlight' );
            $( table.row( rowIdx ).nodes() ).addClass( 'highlight' );
        }
    } ); 

    // handles the unhighlighting of cells on mouseleave
    $('#schedule tbody').on( 'mouseleave', function() {
        $( table.cells().nodes() ).removeClass( 'highlight' );
    } );
    
} );
