$(document).ready(function(){
	$(".expli").click(function(){
		var ul = $(this).siblings("ul");
		if ( ul.css('display') == 'none' ){

	$('.expli').children('.fa').removeClass('fa-plus-square-o').addClass('fa-minus-square-o');

	ul.show(300);
		}
		else{
			
			
	$('.expli').children('.fa').removeClass('fa-minus-square-o').addClass('fa-plus-square-o');

	ul.hide(300);
		}
	
	
	})
});