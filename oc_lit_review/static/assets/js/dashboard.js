$("#button-ask").click(function () {
  $("#modal-ask").modal("show");
});
$("#button-create").click(function () {
  $("#modal-create").modal("show");
});
$(".btn-reply").click(function () {
  let ticketID = $(this).attr("data-ticket");
  $("#form-ticket-id").val(ticketID);
  $("#modal-reply").modal("show");
});
