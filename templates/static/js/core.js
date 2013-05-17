$(document).ready(function(){
	$("#submit").click(function(){
		$.ajax({
			url:'/Admin/Ajax/Character',
			type: 'get',
			data: $('form').serialize(),
			success: function(resp){
				$('div#c_info').html(resp);
			}
		});
		
	});
	
});
