$(document).ready(function() {
    var lastIdx = null;

    var table = $('#schedule').DataTable( {
        "paging": false,
        "searching": false,
        "info": false,
        "ordering":false,
    } );
    
    //For multiselect checkbox list
    $('.dropdown-menu').on('click', function(e) {
        if($(this).hasClass('dropdown-menu-form')) {
            e.stopPropagation();
        }
    });

    var selectCell = function(cellObj) {
        if ( !$( table.cell(cellObj).node() ).hasClass( 'time' )) {
            var cellTime = $( table.cell(cellObj).node() )
            $( table.cell(cellObj).node() ).addClass( 'select' );

//this code is not working
//            $.post("aggregate",
//                {
//                    "timeStart": cellTime.toString()
//                },
//                function(data, status) {
//                    alert("Data: " + data + "\nStatus: " + status);
//                });
        }
    }

    var selectAllCells = function() {
        for (var i = 1; i < 8; i++) {
            $( table.column(i).nodes() ).addClass( 'select' );
        }
    }

    var deselectAllCells = function() {
        for (var i = 1; i < 8; i++) {
            $( table.column(i).nodes() ).removeClass( 'select' );
        }
    }

    var removeSelectCell = function(cellObj) {
        $( table.cell(cellObj).node() ).removeClass( 'select' );
    }
        

    $('#schedule tbody')
        .on( 'mouseover', 'td', function() {
            var colIdx = table.cell(this).index().column;

            if ( colIdx !== lastIdx && colIdx !== 0 ) {
                $( table.cells().nodes() ).removeClass( 'highlight' );
                $( table.column( colIdx ).nodes() ).addClass( 'highlight' );
            }
        } )
        .on( 'mouseleave', function() {
            $( table.cells().nodes() ).removeClass( 'highlight' );
        } )
        .on( 'click', 'td', function() {
            //makes cells have select properties if they do not already have
            // select properties and also are not part of the time class.
            // If they do have select class clicking removes the select class
            if ( $( table.cell(this).node() ).hasClass( 'select' )) {
                removeSelectCell(this);
            } else {
                selectCell(this);
            }
        } );

    var cellSwitch = 0;

    $('#schedule thead')
        // if td with class select-all is clicked, all cells are selected
        // except for those with time class. If clicked again, deselects all
        .on( 'click', 'td.select-all', function() {
            if (cellSwitch == 0) {
                selectAllCells();
                cellSwitch++;
            } else {
                deselectAllCells();
                cellSwitch--;
            }
        } );

} );
