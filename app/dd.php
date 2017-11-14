<!DOCTYPE html>
<html lang="en">
<head>
	<meta http-equiv="X-UA-Compatible" content="IE=edge">

	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1" />
	<meta name="description" content="Neon Admin Panel" />
	<meta name="author" content="" />

	<link rel="icon" href="assets/images/favicon.ico">

		<title>Essay Dove | Edit Order </title>

  <?php $this->load->view('admin/common/styles')?>
  <!-- Imported styles on this page -->
	<!--[if lt IE 9]><script src="assets/js/ie8-responsive-file-warning.js"></script><![endif]-->
	
	<!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
	<!--[if lt IE 9]>
		<script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
		<script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
	<![endif]-->


</head>
<body class="page-body" data-url="<?php echo base_url();?>">

<div class="page-container"><!-- add class "sidebar-collapsed" to close sidebar by default, "chat-visible" to make chat appear always -->
	
	
 <?php $this->load->view('admin/common/sidebar')?>

	<div class="main-content">
				
		 <?php $this->load->view('admin/common/header')?>
		
					<ol class="breadcrumb bc-3" >
								<li>
						<a href="<?php echo base_url().'admin/'?>"><i class="fa-home"></i>Home</a>
					</li>
						<li class="active">
									<strong>Edit User</strong>
							</li>
							</ol>
					
	
  <?php echo $message ?>
		
		<div class="panel panel-primary">
		  
    

			<div class="panel-body">
		
				<form role="form" id="form1" action="<?php echo base_url().'admin/orders/edit/'.$order['order_id'] ?>" method="post" class="validate" enctype="multipart/form-data">
		
					<div class="form-group">
						<label class="control-label">Order #</label>
						<input type="text" class="form-control" name="order_id" value="<?php echo $order['order_id'] ?>" data-validate="required" data-message-required="First Name is Required" placeholder="First Name" />
					</div>
          
          <div class="form-group">
						<label class="control-label">Date</label>
						<input type="text" class="form-control" name="date" value="<?php echo $order['date'] ?>" data-validate="required" data-message-required="Last Name is Required" placeholder="First Name" />
					</div>
		
					<div class="form-group">
						<label class="control-label">Paper Type</label>
		
						<input type="text" class="form-control" name="paper_type" value="<?php echo $order['paper_type'] ?>" data-validate="required"  data-message-required="Paper Type" placeholder="Email Address" />
					</div>
					
					
					<div class="form-group">
						<label class="control-label">Topic</label>
						<input type="text" class="form-control" name="topic" value="<?php echo $order['topic'] ?>" data-validate="required" data-message-required="Topic" placeholder="First Name" />
					</div>
					
					
					 <div class="form-group">
						<label class="control-label">Instructions</label>
						<textarea style="height:250px;text-align:left"  class="form-control" name="instructions">
					       <?php echo $order['instructions']; ?>
						 </textarea> 
					</div>
					
					   <div class="form-group">
								<label class="control-label">File Attachments</label>
								<div >
									<?php
											foreach($map as $file){
													 echo '<i class="entypo-attach"></i><a href="'.base_url().'uploads/'.$order['order_id'].'/'.$file.'">'.$file.'</a>  <a title="Delete File" onclick="delete_file("'.$order['order_id'].'","'.$file.'")"><i class="entypo-trash"></i></a><br>';
											}
									?>
								</div>
							 
							   <input type="file" placeholder="File*" class="form-control" id="multiFiles" name="files[]" multiple/>
                                  
						</div>
					
					
					<div class="form-group">
						<label class="control-label">Last Name</label>
						<input type="text" class="form-control" name="format" value="<?php echo $order['format'] ?>" data-validate="required" data-message-required="Format is Required" placeholder="First Name" />
					</div>
					
						
					<div class="form-group">
						<label class="control-label">Deadline</label>
						<input type="text" class="form-control" name="deadline" value="<?php echo $order['deadline'] ?>" data-validate="required" data-message-required="Deadline is Required" placeholder="First Name" />
					</div>
					
					
						<div class="form-group">
						<label class="control-label">No. of pages</label>
						<input type="text" class="form-control" name="num_pages" value="<?php echo $order['num_pages'] ?>" data-validate="required" data-message-required="Num of Pages is Required" placeholder="Number of Pages" />
					</div>
					
					<div class="form-group">
						<label class="control-label">Amount</label>
						<input type="text" class="form-control" name="amount" value="<?php echo $order['amount'] ?>" data-validate="required" data-message-required="Amount is Required" placeholder="First Name" />
					</div>
					
					
					<div class="form-group">
						<label class="control-label">Order Status</label>
						<input type="text" class="form-control" name="status" value="<?php echo $order['status'] ?>" data-validate="required" data-message-required="Amount is Required" placeholder="First Name" />
					</div>
					
						<div class="form-group">
						<label class="control-label">Client Email</label>
						<input type="text" class="form-control" name="email" value="<?php echo $order['email'] ?>" data-validate="required" data-message-required="Amount is Required" placeholder="First Name" />
					</div>

					<div class="form-group">
						<button type="submit" class="btn btn-success">Save</button>
					</div>
		
				</form>
		
			</div>
		
		</div>
		<!-- Footer -->

    <?php $this->load->view('admin/common/footer')?>
	</div>

</div>




	<!-- Bottom scripts (common) -->
<?php $this->load->view('admin/common/scripts')?>
  
	
  
	<!-- Imported scripts on this page -->
	<script src="<?php echo base_url();?>static/admin/assets/js/jquery.validate.min.js"></script>
  <script src="<?php echo base_url();?>static/vendor/intl-tel-input/js/intlTelInput.js"></script>


	<!-- JavaScripts initializations and stuff -->
	<script src="<?php echo base_url();?>static/admin/assets/js/neon-custom.js"></script>


	<!-- Demo Settings -->
	<script src="<?php echo base_url();?>static/admin/assets/js/neon-demo.js"></script>
  
  <script type="text/javascript">
	  $("#phone").intlTelInput({
	  initialCountry: "auto",
	  geoIpLookup: function(callback) {
		$.get('https://ipinfo.io', function() {}, "jsonp").always(function(resp) {
		  var countryCode = (resp && resp.country) ? resp.country : "";
		  callback(countryCode);
		});
	  },
	  utilsScript: "<?php echo base_url();?>static/vendor/intl-tel-input/js/utils.js" // just for formatting/placeholders etc
	});	   
	$("#phone").intlTelInput("setNumber", "<?php echo $user->phone ?>");
	
	$("form").submit(function(){
			$('#phone').val($("#phone").intlTelInput("getNumber"));
	});
		
		 function delete_file(id,file){
			swal({
					title: 'Are you sure?',
					text: "You won't be able to revert this!",
					type: 'warning',
					showCancelButton: true,
					confirmButtonColor: '#3085d6',
					cancelButtonColor: '#d33',
					confirmButtonText: 'Yes, delete it!'
				}).then(function () {
				   var url = "<?php echo base_url().'/admin/order/delete'?>";
					 window.location= url+"/"+id;
				});
		}
	</script>
	

	
	

</body>
</html>