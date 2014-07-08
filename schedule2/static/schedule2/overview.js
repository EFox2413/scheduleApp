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
    
    //populates cells with tutor names based on inputs
    function populateCells(name, day, start, end) {
        column = null;
        rowStart = null;
        rowEnd = null;

        for (var colIdx = firstColumn + 1; colIdx < lastColumn; colIdx++) {
            if ( day == $( table.column( colIdx ).header() ).text() ) {
                column = colIdx;
            }
        }

        for (var rowIdx = firstRow; rowIdx < lastRow; rowIdx++) {
            if ( start == $( table.cells(rowIdx, firstColumn).nodes() ).text() ) {
                rowStart = rowIdx
            }
            if ( end == $( table.cells(rowIdx, firstColumn).nodes() ).text() ) {
                rowEnd = rowIdx
            }
        }

        for (var rowIdx = rowStart; rowIdx < rowEnd; rowIdx++) {
            if (name != null && column != null && rowStart != null) {
                $( table.cells(rowIdx, column).nodes() ).append(name + ", ");
            }
        }
    }

    // gets data using AJAX GET request
    $.get("data/", function(response, status) {
        responseArray = response.split("\n");
        itemArray = [];

        for (var i in responseArray) {
            alert(responseArray[i]);
            item = responseArray[i].split(",");
            populateCells(item[0], item[1], item[2], item[3]);
        }

    });

    // adds disabled class to certain cells, specific for this institution
    function disableCells() {
        $( table.column(7).nodes() ).addClass('disabled');
        
        for (var rowIndex = firstRow; rowIndex < firstRow + 5; rowIndex++) {
            $( table.cells(rowIndex, 6).nodes() ).addClass('disabled');
        }

        for (var rowIndex = lastRow - 11; rowIndex < lastRow; rowIndex++) {
            $( table.cells(rowIndex, 6).nodes() ).addClass('disabled');
        }

        for (var rowIndex = lastRow - 5; rowIndex < lastRow; rowIndex++) {
            $( table.cells(rowIndex, 5).nodes() ).addClass('disabled');
        }

        // last row of each column, except for time column
        for (var colIndex = firstColumn + 1; colIndex < lastColumn; colIndex++) {
            $( table.cells(lastRow - 1, colIndex).nodes() ).addClass('disabled');
        }
    }

    disableCells();

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
