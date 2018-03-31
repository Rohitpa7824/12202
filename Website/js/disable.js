$(document).ready(function(){
        $(".cult").click(function () {
            if ($(this).is(":checked")) {
                $("#categories").hide();
                $('.cult').not(this).prop('checked', false);
                console.log($('.cult').not(this));  
            }
            else{
            	$("#categories").show();
            }
        });
        $(".income").click(function () {
            if ($(this).is(":checked")) {
                $("#categories").hide();
                $('.income').not(this).prop('checked', false); 
            }
            else{
            	$("#categories").show();
            }
        });
        $(".parent").click(function () {
            if ($(this).is(":checked")) {
                $("#categories").hide();
                $('.parent').not(this).prop('checked', false); 
            }
            else{
            	$("#categories").show();
            }
        });
    });