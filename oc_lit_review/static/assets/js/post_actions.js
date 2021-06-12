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
            $("#modal-ticket").modal("show");
        }
    });
});
$("#button-create").click(function () {
  $.ajax({
        url: "/get_modal_full_review",
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
        url: "/get_modal_simple_review",
        type: "GET",
        dataType: "html",
        success: function (data) {
            $("#modal-wrapper").html(data);
        },
        error: function (xhr, status) {
            alert("Une erreur est survenue.");
        },
        complete: function (xhr, status) {
            $("#form-ticket-id").val(postID);
            $("#modal-simple-review").modal("show");
        }
    });
});

$(".btn-edit-ticket").click(function () {
  let postID = $(this).attr("data-postid");
  $.ajax({
        url: "/get_modal_ticket/" + postID,
        type: "GET",
        dataType: "html",
        success: function (data) {
            $("#modal-wrapper").html(data);
        },
        error: function (xhr, status) {
            alert("Une erreur est survenue.");
        },
        complete: function (xhr, status) {
            let hiddenField = "<input type='hidden' name='ticket-id' value='"+postID+"'/>"
            $("#form-ticket").prepend(hiddenField)
            $('#form-ticket').attr('action', '/make_ticket/'+postID);
            $("#modal-ticket").modal("show");
        }
    });
});

$(".btn-edit-review").click(function () {
  let postID = $(this).attr("data-postid");
  $.ajax({
        url: "/get_modal_simple_review/" + postID,
        type: "GET",
        dataType: "html",
        success: function (data) {
            $("#modal-wrapper").html(data);
        },
        error: function (xhr, status) {
            alert("Une erreur est survenue.");
        },
        complete: function (xhr, status) {
            let hiddenField = "<input type='hidden' name='review-id' value='"+postID+"'/>"
            $("#form-review").prepend(hiddenField)
            $('#form-review').attr('action', '/make_simple_review/'+postID);
            $("#modal-simple-review").modal("show");
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