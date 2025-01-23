const Elements = {
  email: document.getElementById("email"),
  xname: document.getElementById("xname"),
  submitbtn: document.getElementById("submitbtn"),
};

const validateEmailField = () => {
  const isValid = validator.isEmail(Elements.email.value);

  if (isValid) {
    Elements.email.classList.add("border-blue-1");
    Elements.email.classList.remove("focus:border-black");
  } else {
    Elements.email.classList.remove("border-blue-1");
    Elements.email.classList.add("focus:border-black");
  }
  return isValid;
};

const validateXnameField = () => {
  xname = Elements.xname;
  const isEmpty = validator.isEmpty(xname.value);
  if (isEmpty) {
    xname.classList.add("focus:border-black");
    xname.classList.remove("border-blue-1");
  } else {
    xname.classList.remove("focus:border-black");
    xname.classList.add("border-blue-1");
  }
  return !isEmpty;
};

const enableButton = () => {
  const btn = Elements.submitbtn;
  const isValid = validateEmailField() && validateXnameField();

  if (isValid) {
    btn.disabled = !isValid;
    btn.classList.toggle("disabled:cursor-not-allowed");
    btn.classList.add("bg-blue-1");
    btn.classList.remove("bg-gray-bold");
  } else {
    btn.disabled = !isValid;
    btn.classList.add("disabled:cursor-not-allowed");
    btn.classList.remove("bg-blue-1");
    btn.classList.add("bg-gray-bold");
  }
};

Elements.email.addEventListener("input", () => {
  validateEmailField();
  enableButton();
});
Elements.xname.addEventListener("input", () => {
  validateXnameField();
  enableButton();
});
