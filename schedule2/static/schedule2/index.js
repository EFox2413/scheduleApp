$(document).ready(function() {
    var firstColumn = 0;
    var lastColumn = 8; // index of the last column
    var firstRow = 0;
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

    $('#areas input').change(function(event) {
        var id = $(this).attr('id');
        //alert(id + " was changed");

        // sends an AJAX  post request with data
        $.post("makeSubList/",
            {
                subAreas: id[4],
            },
            function(data, status) {
            });
    });

    // Sends AJAX POST if all forms have acceptable submissions
    $('form').submit(function(event) {
        if (checkSubmission()) {

            var subAreaValues = $('#subAreas li input:checkbox:checked')
              .map(function() {
                var str = $(this).parent().text();
                str = str.replace(/\s\s+/g, '');
                return str;
            }).get();

            var semesterValue = $('input[name=choice]:checked', '#employeeForm')
              .map(function() {
                var str = $(this).next().text();
                str = str.replace(/\s\s+/g, '');
                return str;
            }).get().join('');

            var availabilityValues = $('#schedule tbody')
              .map(function() {
                var availabilityTime = [];

                for (var colIdx = firstColumn + 1; colIdx < lastColumn; colIdx++) {
                    // selectTracker is used to check if there is an end to
//                     consecutive selected cells
                    var selectTracker = false;
                    var weekDay = $( table.column( colIdx ).header() ).text();
                    var timeString = "";

                    for (var rowIdx = firstRow; rowIdx < lastRow; rowIdx++) {
                        var cellIsSelected = $( table.cells(rowIdx, colIdx).nodes() )
                                                     .hasClass( 'select' );
                        var cellTime = $( table.cells( rowIdx, firstColumn ).nodes() ).text();

                        if ( cellIsSelected && !selectTracker ) {
                            selectTracker = true;

                            //get row, get column
                            timeString = weekDay + " " + cellTime;
                        } else if ( !cellIsSelected && selectTracker ) {
                            selectTracker = false;
                            timeString = timeString + " " + cellTime;
                            availabilityTime.push(timeString);
                        }
                    }
                }
                return availabilityTime;
            }).get();

            // sends an AJAX  post request with data on cells selected
            // Name, Area, and Sub-Areas
            $.post("testPost/",
                {
                    'name': document.getElementById('nameInput').value,
                    'subArea': subAreaValues,
                    'semester': semesterValue,
                    'availability': availabilityValues,
                },
                function(data, status) {
                    alert(data, status);
                });
        }
        event.preventDefault();
    });

    // adds disabled class to certain cells, specific for this institution
    function disableCells() {
        $( table.column(7).nodes() ).addClass('disabled');
        
        // saturday
        for (var rowIndex = firstRow; rowIndex < firstRow + 5; rowIndex++) {
            $( table.cells(rowIndex, 6).nodes() ).addClass('disabled');
        }

        // saturday
        for (var rowIndex = lastRow - 11; rowIndex < lastRow; rowIndex++) {
            $( table.cells(rowIndex, 6).nodes() ).addClass('disabled');
        }

        // for friday
        for (var rowIndex = lastRow - 5; rowIndex < lastRow; rowIndex++) {
            $( table.cells(rowIndex, 5).nodes() ).addClass('disabled');
        }
        
        // last row of each column, except for time column
        for (var colIndex = firstColumn + 1; colIndex < lastColumn; colIndex++) {
            $( table.cells(lastRow - 1, colIndex).nodes() ).addClass('disabled');
        }
    }

    disableCells();

    // adds select class to a cell
    function selectCell(rowIdx, colIdx) {
        if ( !$( table.cells(rowIdx, colIdx).nodes() ).hasClass( 'time' ) &
             !$( table.cells(rowIdx, colIdx).nodes() ).hasClass( 'disabled' )) {
            $( table.cells(rowIdx, colIdx).nodes() ).addClass( 'select' );
        }
    }

    // removes select class from a cell
    function removeSelectCell(cellObj) {
        $( table.cells(cellObj).nodes() ).removeClass( 'select' );
    }

    // when a cell is clicked if it does not have select class calls 
    // selectCell()
    $('#schedule tbody').on( 'click', 'td', function() {
        var colIdx = table.cell(this).index().column;
        var rowIdx = table.cell(this).index().row;

        if ( $( table.cell(this).node() ).hasClass( 'select' )) {
            removeSelectCell(this);
        } else {
            selectCell(rowIdx, colIdx);
        }
    } );

    // adds select class to a row of cells
    function selectRowOfCells(rowIdx) {
        for (var i = 1; i < lastColumn; i++) {
            selectCell(rowIdx, i);
        }
    }

    // removes select class from a row of cells
    function deselectRowOfCells(rowId) {
        for (var i = 1; i < lastColumn; i++) {
            $( table.cells(rowId, i).nodes() ).removeClass( 'select' );
        }
    }

    function checkSelect(rowIdx, colIdx) {
        if ( $( table.cells(rowIdx, colIdx).nodes() ).hasClass( 'select' ) ||
             $( table.cells(rowIdx, colIdx).nodes() ).hasClass( 'disabled' ) ) {
            return true;
        }

        return false;
    }

    // selects a row of cells on click, deselects only if all cells in
    // row are already selected
    $('#schedule tbody').on( 'click', 'td.time', function() {
        var rowIdx = table.cell(this).index().row;
        var selected = true;

        for (var columnIndex = 1; columnIndex < lastColumn; columnIndex++) {

            if ( !checkSelect(rowIdx, columnIndex) ) {
                selected = false;
            }
        }

        if ( selected ) {
            deselectRowOfCells(rowIdx);
        } else {
            selectRowOfCells(rowIdx);
        }
    });

    // adds select class to a column of cells
    function selectColumnOfCells(colId) {
        for (var rowIndex = firstRow; rowIndex < lastRow; rowIndex++) {
            selectCell(rowIndex, colId);
        }
    }

    // removes select class from a column of cells
    function deselectColumnOfCells(colId) {
        for (var rowIndex = firstRow; rowIndex < lastRow; rowIndex++) {
            $( table.cells(rowIndex, colId).nodes() ).removeClass( 'select' );
        }
    }

    // selects a column of cells on click, deselects only if all cells in
    // column are already selected.
    $('#schedule').on( 'click', 'td.days', function() {
        var colIdx = table.column(this).index();
        var selected = true;

        for (var rowIndex = 0; rowIndex < lastRow; rowIndex++) {

            if ( !checkSelect(rowIndex, colIdx) ){
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
        for (var colIndex = firstColumn; colIndex < lastColumn; colIndex++) {
            selectColumnOfCells(colIndex);
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
    } ); 

    // handles the unhighlighting of cells on mouseleave
    $('#schedule tbody').on( 'mouseleave', function() {
        $( table.cells().nodes() ).removeClass( 'highlight' );
    } );
    
} );
