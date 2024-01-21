    $(document).ready(function () {
        $('.open-modal').on('click', function () {
            $.ajax({
                url: '/projects/create',
                type: 'GET',
                success: function (data) {
                    $('#modal-content').html(data);
                    $('#create-modal').modal('show');
                },
                error: function () {
                    $('#modal-content').html(this.error);
                    $('#create-modal').modal('show');
                }
            });
        });
    });