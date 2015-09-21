var app = angular.module('myapp', []);
app.controller('myCtrl', function($scope,$http) {
    $http.get("http://localhost:8000/cashpoint/productlist").success(
       function(response){
$scope.Product=response;

       }

        );
    
});