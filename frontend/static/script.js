function updateUnitOptions() {
  const category = document.getElementById("category").value;
  const unitFrom = document.getElementById("unit_from");
  const unitTo = document.getElementById("unit_to");

  unitFrom.innerHTML = "";
  unitTo.innerHTML = "";

  const units = {
    "length": ["meter", "kilometer", "cm", "inches", "feet"],
    "weight": ["kg", "pounds", "g", "ounces"],
    "temperature": ["Celsius", "Fahrenheit", "Kelvin"],
    "storage": ["KB", "MB", "GB", "TB", "bytes"],
    "speed": ["m/s", "km/h", "mph", "ft/s"],
    "volume": ["L", "mL", "gal", "in³"],
    "area": ["m²", "km²", "ft²", "in²", "cm²"],
    "time": ["second", "minute", "hour", "day", "week", "month", "year"]
  };
  if (!units[category]) return;

  const defaultOptionFrom = document.createElement("option");
  defaultOptionFrom.value = "";
  defaultOptionFrom.text = "Select Unit";
  defaultOptionFrom.disabled = true;
  defaultOptionFrom.selected = true;

  const defaultOptionTo = defaultOptionFrom.cloneNode(true);

  unitFrom.appendChild(defaultOptionFrom);
  unitTo.appendChild(defaultOptionTo);

  units[category].forEach(unit => {
    const optionFrom = document.createElement("option");
    optionFrom.value = unit;
    optionFrom.text = unit;
    const optionTo = optionFrom.cloneNode(true);
    unitFrom.appendChild(optionFrom);
    unitTo.appendChild(optionTo);
  });
}

async function convert() {
  const valueField = document.getElementById("value");
  const value = parseFloat(valueField.value);
  const fromUnit = document.getElementById("unit_from").value;
  const toUnit = document.getElementById("unit_to").value;
  const category = document.getElementById("category").value;

  if (isNaN(value)) {
    alert("Please enter a valid number!");
    valueField.focus();
    return;
  }
  if (!category) {
    alert("Please select a category!");
    document.getElementById("category").focus();
    return;
  }
  if (!fromUnit) {
    alert("Please select a 'From' unit!");
    document.getElementById("unit_from").focus();
    return;
  }
  if (!toUnit) {
    alert("Please select a 'To' unit!");
    document.getElementById("unit_to").focus();
    return;
  }

  try {
    const response = await fetch(
      `/convert?value=${encodeURIComponent(value)}&unit_from=${encodeURIComponent(
        fromUnit
      )}&unit_to=${encodeURIComponent(toUnit)}&category=${encodeURIComponent(
        category
      )}`
    );
    if (!response.ok) throw new Error("Conversion service error");
    const data = await response.json();

    displayConvertedValue(data.converted_value, toUnit);
  } catch (err) {
    alert("Error: " + err.message);
  }
}

function displayConvertedValue(value, unit) {
  const convertedValueDiv = document.querySelector(".result");
  let formattedValue =
    typeof value === "number" ? Number(value.toFixed(6)) : value;
  convertedValueDiv.textContent = `${formattedValue} ${unit}`;
}

function updateYear() {
  document.getElementById("year").textContent = new Date().getFullYear();
}

window.onload = () => {
  updateUnitOptions();
  updateYear();
  document.getElementById("category").addEventListener("change", updateUnitOptions);
  document.getElementById("convertBtn").addEventListener("click", convert);
};