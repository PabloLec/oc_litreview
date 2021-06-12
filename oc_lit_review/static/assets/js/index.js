$("#button-login").click(function () {
  $("#modal-login").modal("show");
});
$("#button-signup").click(function () {
  $("#modal-signup").modal("show");
});
var toastElList = [].slice.call(document.querySelectorAll(".toast"));
var toastList = toastElList.map(function (toastEl) {
  return new bootstrap.Toast(toastEl);
});

for (const x of toastList) {
  x.show();
}

var CSRFToken = document.getElementsByName("csrfmiddlewaretoken")[0].value

$("#register").validate({
  rules: {
    username: {
      required: true,
      remote: {
        url: "/is_username_available",
        type: "post",
        data: {
          username: function () {
            return $("#username").val();
          },
          csrfmiddlewaretoken: CSRFToken,
        },
      },
    },
    password1: {
      required: true,
      minlength: 8,
    },
    password2: {
      required: true,
      minlength: 8,
      equalTo: "#password1",
    },
  },

  messages: {
    username: {
      required: "Entrez un nom d'utilisateur.",
      remote: "Ce nom d'utilisateur est déjà pris.",
    },
    password1: {
      required: "Entrez votre mot de passe.",
      minlength: "Votre mot de passe doit comporter au moins 8 caractères.",
    },
    password2: {
      required: "Entrez votre mot de passe.",
      minlength: "Votre mot de passe doit comporter au moins 8 caractères.",
      equalTo: "Les mots de passes ne sont pas identiques.",
    },
  },

  submitHandler: function (form) {
    form.submit();
  },
});
