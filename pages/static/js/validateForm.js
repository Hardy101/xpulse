const Elements = {
  email: document.getElementById("email"),
  xname: document.getElementById("xname"),
  submitbtn: document.getElementById("submitbtn"),
};
const validateEmailField = () => {
  return validator.isEmail(Elements.email.value);
};

const enableButton = () => {
  const btn = Elements.submitbtn;
  if (validateEmailField()) {
    btn.disabled = false;
    btn.classList.remove("disabled:cursor-not-allowed");
  } else {
    btn.disabled = true;
    btn.classList.add("disabled:cursor-not-allowed");
  }
};

Elements.email.addEventListener("input", enableButton);
