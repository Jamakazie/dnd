$(document).ready(function(){
	$("#submit").click(function(){
		$.ajax({
			url:'/Admin/Ajax/Character',
			type: 'get',
			data: $('form').serialize(),
			success: function(resp){
				$('div#c_info').html(resp);
				commit();
			}
		});
		
	});
	
});
function commit(){
	$("#commit").click(function(){
		$.ajax({
			url:'/Admin/Ajax/Commit',
			type: 'get',
			success: function(resp){
				if(resp === 'success'){
					$('#commit').remove();
					$('#c_sheet').append('<span class="span2 uneditable-input">Commit Successful</span>');
				}
				else{
					alert("Something bad happened :D" + resp);
				}
			}
		});
	});
}
