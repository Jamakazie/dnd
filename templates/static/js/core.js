$(document).ready(function(){
	$("#submit").click(function(){
		$.ajax({
			url:'/Admin/Ajax/Character',
			type: 'get',
			data: $('form').serialize(),
			success: function(resp){
				alert(resp);
			}
		});
		
	});
	
});
