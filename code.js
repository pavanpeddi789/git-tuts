document.addEventListener("DOMContentLoaded", loadContacts);
document.getElementById("addBtn").addEventListener("click", addContact);

async function loadContacts() {
  const res = await fetch("/contacts");
  const data = await res.json();
  const tbody = document.querySelector("#contactTable tbody");
  tbody.innerHTML = "";

  data.forEach(contact => {
    const row = `
      <tr>
        <td>${contact.contact_id}</td>
        <td>${contact.firstname}</td>
        <td>${contact.lastname}</td>
        <td>${contact.phone}</td>
        <td><button class="delete-btn" onclick="deleteContact(${contact.contact_id})">Delete</button></td>
      </tr>`;
    tbody.insertAdjacentHTML("beforeend", row);
  });
}

async function addContact() {
  const firstname = document.getElementById("firstname").value.trim();
  const lastname = document.getElementById("lastname").value.trim();
  const phone = document.getElementById("phone").value.trim();

  if (!firstname || !lastname || !phone) {
    alert("Please fill all fields!");
    return;
  }

  const res = await fetch("/add", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ firstname, lastname, phone })
  });

  if (res.ok) {
    document.getElementById("firstname").value = "";
    document.getElementById("lastname").value = "";
    document.getElementById("phone").value = "";
    loadContacts();
  }
}

async function deleteContact(id) {
  if (!confirm("Are you sure you want to delete this contact?")) return;
  await fetch(`/delete/${id}`, { method: "DELETE" });
  loadContacts();
}
