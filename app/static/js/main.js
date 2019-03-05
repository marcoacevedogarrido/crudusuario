$(document).ready(function() {

    var table_container = $('#dataTable');
    if (table_container.length > 0) {
        var table = table_container.DataTable({
            data: dataTable,
            columns: [
                { title: "Mes" },
                { title: "Total Ventas" }
            ]
        });

        $("#dataTable tbody").on('click', 'tr', function () {
            var data = table.row(this).data();
            window.location.href = 'http://Xsolution.cl:5071/biVentas/76783666k';
        }).on('mouseover', 'tr', function () {
            $('html,body').css('cursor','pointer');
        }).on('mouseout','tr',function () {
            $('html,body').css('cursor','auto');
        });
    }

});



