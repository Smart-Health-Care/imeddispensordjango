(function () {
    var alertService = angular.module("alertService", ['angularModalService']);

    alertService.factory("alertService", function (ModalService) {

        var o = {};


        o.showAlert = function (message) {

            ModalService.showModal({
                templateUrl: "/static/pos/templates/message_modal.html",
                controller: function ($scope, close, $element,message) {
                    $scope.closeM = function () {
                        $element.modal('hide');
                        close(false,500);
                    };

                    $scope.message = message;

                },
                inputs: {
                    message: message
                }
            }).then(function (modal) {
                modal.element.modal();

            });

        };


        return o;

    });

})();