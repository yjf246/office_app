function filterTable() {
    const filterValues = {};
    const table = document.getElementById('myTable');
    const rows = table.getElementsByTagName('tr');



    for (let i = 0; i < rows[0].cells.length; i++) {
        const selectElement = document.getElementById(`filter_${i}`);
        const selectedValue = selectElement.value.toLowerCase();
        if (selectedValue !== '') {
            filterValues[i] = selectedValue;
        }
    }1

    for (let i = 1; i < rows.length; i++) {
        const row = rows[i];
        let isVisible = true;

        for (let j = 0; j < row.cells.length; j++) {
            const cell = row.cells[j];
            const cellValue = cell.innerHTML.toLowerCase();

            if (filterValues[j] && cellValue.indexOf(filterValues[j]) === -1) {
                isVisible = false;
                break;
            }
        }

        row.style.display = isVisible ? '' : 'none';
    }
}
const table = document.getElementById('myTable');
const headerRow = table.getElementsByTagName('tr')[0];

for (let i = 0; i < headerRow.cells.length; i++) {
    const distinctValues = new Set();

    // Collect distinct values in the column
    for (let j = 1; j < table.rows.length; j++) {
        const cellValue = table.rows[j].cells[i].textContent;
        distinctValues.add(cellValue);
    }

    // Create a select element for filtering
    const select = document.createElement('select');
    select.id = `filter_${i}`;
    select.classList.add('filter');
    select.addEventListener('change', filterTable);

    // Add an empty option as the default selection
    const emptyOption = document.createElement('option');
    emptyOption.value = '';
    emptyOption.textContent = 'All';
    select.appendChild(emptyOption);

    // Create an option for each distinct value in the column
    distinctValues.forEach((value) => {
        const option = document.createElement('option');
        option.value = value;
        option.textContent = value;
        select.appendChild(option);
    });

    // Insert the select element into the table header
    headerRow.cells[i].appendChild(select);
}
function sortTable(column) {
    var table, rows, switching, i, x, y, shouldSwitch, dir, switchcount = 0;
    table = document.getElementById("myTable");
    switching = true;
    dir = "asc"; // Set the default sorting direction to ascending

    while (switching) {
        switching = false;
        rows = table.rows;

        for (i = 1; i < (rows.length - 1); i++) {
            shouldSwitch = false;
            x = rows[i].getElementsByTagName("TD")[column];
            y = rows[i + 1].getElementsByTagName("TD")[column];

            if (dir == "asc") {
                if (x.innerHTML.toLowerCase() > y.innerHTML.toLowerCase()) {
                    shouldSwitch = true;
                    break;
                }
            } else if (dir == "desc") {
                if (x.innerHTML.toLowerCase() < y.innerHTML.toLowerCase()) {
                    shouldSwitch = true;
                    break;
                }
            }
        }

        if (shouldSwitch) {
            rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
            switching = true;
            switchcount++;
        } else {
            if (switchcount == 0 && dir == "asc") {
                dir = "desc";
                switching = true;
            }
        }
    }
}
