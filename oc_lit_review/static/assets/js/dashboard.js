$("#button-ask").click(function () {
  $.ajax({
        url: "/get_modal_ticket",
        type: "GET",
        dataType: "html",
        success: function (data) {
            $("#modal-wrapper").html(data);
        },
        error: function (xhr, status) {
            alert("Une erreur est survenue.");
        },
        complete: function (xhr, status) {
            $("#modal-ask").modal("show");
        }
    });
});
$("#button-create").click(function () {
  $.ajax({
        url: "/get_modal_review",
        type: "GET",
        dataType: "html",
        success: function (data) {
            $("#modal-wrapper").html(data);
        },
        error: function (xhr, status) {
            alert("Une erreur est survenue.");
        },
        complete: function (xhr, status) {
            $("#modal-create").modal("show");
        }
    });
});
$(".btn-reply").click(function () {
  let postID = $(this).attr("data-postid");
  $.ajax({
        url: "/get_modal_ticket_response",
        type: "GET",
        dataType: "html",
        success: function (data) {
            $("#modal-wrapper").html(data);
        },
        error: function (xhr, status) {
            alert("Une erreur est survenue.");
        },
        complete: function (xhr, status) {
            $("#form-ticket-id").val(ticketID);
            $("#modal-reply").modal("show");
        }
    });
});

$(".btn-edit").click(function () {
  let postID = $(this).attr("data-postid");
  $.ajax({
        url: "/get_modal_ticket/" + ticketID,
        type: "GET",
        dataType: "html",
        success: function (data) {
            $("#modal-wrapper").html(data);
        },
        error: function (xhr, status) {
            alert("Une erreur est survenue.");
        },
        complete: function (xhr, status) {
            let hiddenField = "<input type='hidden' name='ticket-id' value='"+ticketID+"'/>"
            $("#form-ask").prepend(hiddenField)
            $('#form-ask').attr('action', '/ask_review/'+ticketID);
            $("#modal-ask").modal("show");
        }
    });
});

$(".btn-delete").on("click", function (event) {
if (!(confirm('Voulez vous supprimer définitivement cette publication ?'))) {
  return none
}
  event.preventDefault();
  let postID = $(this).attr("data-postid");
  let postType = $(this).attr("data-type");
  let token = $(this).attr("data-token");
  var form = $(
    '<form action="/delete_post/'+postType+'/'+postID+'" method="post">' +
      '<input name="csrfmiddlewaretoken" type="hidden" value="'+token+'"/>' +
      "</form>"
  );
  $("body").append(form);
  form.submit();
});