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
  const isValid = validateEmailField();

  if (isValid) {
    btn.disabled = !isValid;
    btn.classList.toggle("disabled:cursor-not-allowed");
    btn.classList.add("bg-blue-1");
    btn.classList.remove("bg-gray-bold");
    Elements.email.classList.add("border-blue-1");
    Elements.email.classList.remove("focus:border-black");
  } else {
    btn.disabled = !isValid;
    btn.classList.add("disabled:cursor-not-allowed");
    btn.classList.remove("bg-blue-1");
    btn.classList.add("bg-gray-bold");
    Elements.email.classList.add("border-blue-1");
  }
};

Elements.email.addEventListener("input", enableButton);
