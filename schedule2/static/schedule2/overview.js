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
