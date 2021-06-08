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
