const notAUserMessage = `<div class="toast-container position-fixed bottom-0 end-0 p-3" style="z-index: 5">
      	      <div class="toast bg-danger text-white" role="alert" aria-live="assertive" aria-atomic="true">
      	        <div class="toast-header">
      	          <img src="" class="rounded me-2" alt="" />
      	          <strong class="me-auto">Erreur</strong>
      	          <button type="button" class="btn-close" data-bs-dismiss="toast" aria-label="Close"></button>
      	        </div>
      	        <div class="toast-body">Ce nom d'utilisateur n'existe pas.</div>
      	      </div>
      	    </div>`;

const lowerCaseUsers = availableUsers.map((name) => name.toLowerCase());

$("#subscribe-top-btn").on("click", function (event) {
  event.preventDefault();
  let inputContent = document.getElementById("search-user").value;
  let token = document.getElementById("csrf-token").textContent;
  if (inputContent == "") {
    return;
  } else if (lowerCaseUsers.includes(inputContent.toLowerCase())) {
    var form = $(
      '<form action="/follow" method="post" style="display:none">' +
        '<input name="csrfmiddlewaretoken" type="hidden" value="' +
        token +
        '"/>' +
        '<input type="text" name="add" value="' +
        inputContent +
        '" />' +
        "</form>"
    );
    console.log(form);
    $("body").append(form);
    form.submit();
  } else {
    document.getElementById("toast-list").innerHTML = notAUserMessage;
    showToast();
  }
});

$(".btn-subscribe").on("click", function (event) {
  event.preventDefault();
  let user = event.currentTarget.dataset.user;
  let token = document.getElementById("csrf-token").textContent;
  var form = $(
    '<form action="/follow" method="post" style="display:none">' +
      '<input name="csrfmiddlewaretoken" type="hidden" value="' +
      token +
      '"/>' +
      '<input type="text" name="add" value="' +
      user +
      '" />' +
      "</form>"
  );
  $("body").append(form);
  form.submit();
});

$(".btn-unsubscribe").on("click", function (event) {
  event.preventDefault();
  let user = event.currentTarget.dataset.user;
  let token = document.getElementById("csrf-token").textContent;
  var form = $(
    '<form action="/follow" method="post" style="display:none">' +
      '<input name="csrfmiddlewaretoken" type="hidden" value="' +
      token +
      '"/>' +
      '<input type="text" name="delete" value="' +
      user +
      '" />' +
      "</form>"
  );
  $("body").append(form);
  form.submit();
});

function showToast() {
  var toastElList = [].slice.call(document.querySelectorAll(".toast"));
  var toastList = toastElList.map(function (toastEl) {
    return new bootstrap.Toast(toastEl);
  });

  for (const x of toastList) {
    x.show();
  }
}
