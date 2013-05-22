$(document).ready(function(){
	$(document).on('click', '#commit', function(){
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
	$(document).on('click', '#submit', function(){
		$.ajax({
			url:'/Admin/Ajax/Character',
			type: 'get',
			data: $('form').serialize(),
			success: function(resp){
				$('div#c_info').html(resp);
			}
		});
		
	});
	$(document).on('click', '.ajax_view', function(){
		id = $(this).attr('id');
		$.ajax({
			url: '/Admin/Ajax/View/' + id,
			type: 'get',
			success: function(resp){
				$('div#characters').html(resp);
			}
		});
	});
	$(document).on('click', '#person_submit', function(){
		$.ajax({
			url:'/Admin/Ajax/Person/NoSheet',
			data : $("#create_person").serialize(),
			type : 'post',
			success: function(resp){
				alert(resp)
			}
		});

	});
	$(document).on('click', '#person_submit_sheet', function(){
		$.ajax({
			url:'/Admin/Ajax/Person/Sheet',
			data : $("#create_person").serialize(),
			type : 'post',
			success: function(resp){
				alert(resp)
			}
		});

	});

	$(document).on('click', '#person_sheet', function(){
		$.ajax({
			url: '/Admin/Ajax/Sheet',
			type: 'get',
			success: function(resp){
				$('#create_person_sheet').html(resp);
				$("<style>").text("#commit { display:none; }").appendTo("head");
				$("#person_submit").attr('id', 'person_submit_sheet');
			}
		});
	});

	$(document).on('click', '.ajax_people', function(){
		id = $(this).attr('id');
		$.ajax({
			url: '/Admin/Ajax/Person/View/' + id,
			type: 'get',
			success: function(resp){
				$("#people").html(resp);
			}
		});
	});
	$(document).on('click', '.people_ajax_view', function(){
		id = $(this).attr('id');
		$.ajax({
			url: '/People/Person/' + id,
			type: 'get',
			success: function(resp){
				$('#people_view').html(resp)
			}
		});
	});
	$(document).on('click', '.race_update', function(){
		$.ajax({
			url: '/Admin/Ajax/Update/Race/',
			data: $("#race_edit").serialize(),
			type: 'post',
			success: function(resp){
				alert(resp);
			}
		});
	});


});
