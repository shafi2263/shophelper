
var app = angular.module('myapp', []).config(function ($interpolateProvider, $httpProvider) {
    // Force angular to use square brackets for template tag
    // The alternative is using {% verbatim %}
    $interpolateProvider.startSymbol('[[').endSymbol(']]');

    // CSRF Support
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';});
app.controller('myCtrl', function($scope,$http) {
    $http.get(""http://localhost:8000/cashpoint/productlist"").success(
       function(response){
$scope.mydata=response;

       }

        );
    
});