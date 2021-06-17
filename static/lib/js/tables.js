(function ($) {

    'use strict';

    // ------------------------------------------------------- //
    // Auto Hide
    // ------------------------------------------------------ //

    $(function () {
        $('#export-table').DataTable({
            dom: 'Bfrtip',
            "order": [[ 0, "desc" ]],
            language:
                {
                    "sEmptyTable": "Cədvəldə heç bir məlumat yoxdur",
                    "sInfo": " _TOTAL_ Nəticədən _START_ - _END_ Arası Nəticələr",
                    "sInfoEmpty": "Nəticə Yoxdur",
                    "sInfoFiltered": "( _MAX_ Nəticə İçindən Tapılanlar)",
                    "sInfoPostFix": "",
                    "sInfoThousands": ",",
                    "sLengthMenu": "Səhifədə _MENU_ Nəticə Göstər",
                    "sLoadingRecords": "Yüklənir...",
                    "sProcessing": "Gözləyin...",
                    "sSearch": "Axtarış:",
                    "sZeroRecords": "Nəticə Tapılmadı.",
                    "oPaginate": {
                        "sFirst": "İlk",
                        "sLast": "Axırıncı",
                        "sNext": "Sonraki",
                        "sPrevious": "Öncəki"
                    },
                    "oAria": {
                        "sSortAscending": ": sütunu artma sırası üzərə aktiv etmək",
                        "sSortDescending": ": sütunu azalma sırası üzərə aktiv etmək"
                    }

                },
            buttons: {
                buttons: [, {
                    extend: 'excel',
                    text: 'Excel',
                    title: $('h1').text(),
                    exportOptions: {
                        columns: ':not(.no-print)'
                    },
                    footer: true
                }, {
                    extend: 'pdf',
                    text: 'Pdf',
                    title: $('h1').text(),
                    exportOptions: {
                        columns: ':not(.no-print)'
                    },
                    footer: true
                }, {
                    extend: 'print',
                    text: 'Çap Et',
                    title: $('h1').text(),
                    exportOptions: {
                        columns: ':not(.no-print)'
                    },
                    footer: true,
                    autoPrint: true
                }],
                dom: {
                    container: {
                        className: 'dt-buttons'
                    },
                    button: {
                        className: 'btn btn-primary'
                    }
                }
            }
        });
    });

})(jQuery);