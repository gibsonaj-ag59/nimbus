const input_element = document.getElementById("format-file-upload");
var dtime_format_link = document.createElement('a')
dtime_format_link.innerHTML = "datetime.strptime(<button type='button' class='btn btn-outline-primary'>format</button>)-> datetime.datetime"
const formatFunctions = {
    'integer': 'int() -> int',
    'float': 'float() -> float',
    'datetime': dtime_format_link,
    'hex': 'int(xx, 16) -> int',
    'string': 'str() -> str'
};

function fileHandler() {
    const fileList = this.files;
    const extensionsList = ['json', 'csv', 'slk'];
    const handlerFunctions = {
        'csv': analzeCSV,
    };
    for (var i=0; i < fileList.length; i++){
        if (extensionsList.includes(fileList[i].name.split('.')[1])) {
            var name = fileList[i].name
            var type = fileList[i].name.split('.')[1];
            const reader = new FileReader();
            reader.onload = function(e){
                const fileContent = e.target.result;
                updateTable(name, handlerFunctions[type](fileContent));
            }
            reader.readAsText(fileList[i]);
            
        }
    }
}

function analzeCSV(file) {
    lines = file.split('\n').slice(3);
    lines.splice(1,1);
    for (var i = 0; i < lines.length; i ++) {
        lines[i] = lines[i].split(',');
    }
    return lines;
}

function updateTable(name, lines) {
    const results_element = document.getElementById("result-table");
    let row = results_element.insertRow();
    let nam = row.insertCell();
    nam.innerHTML = name;
    let cols = row.insertCell();
    cols.innerHTML = lines[0].length;
    let rows = row.insertCell();
    rows.innerHTML = lines.length;
    let dtypes = row.insertCell();
    let columnTypeCounts = arrayParseValueCount(lines);
    let prob_count = 0
    for (var key in columnTypeCounts){
        val = Object.keys(columnTypeCounts[key]).length;
        if (val > 1 || val == 0) {
            prob_count++
        }
    }
    dtypes.innerHTML = "Detected " + prob_count + " columns with issues."
    let corrections = row.insertCell();
    let button = document.createElement("button");
    button.type = "button"
    button.classList.add("btn", "btn-outline-primary");
    button.setAttribute('data-bs-toggle', 'modal');
    button.setAttribute('data-bs-target', '#dataTypesModal');
    if (prob_count > 0) {
        button.innerText = "Correct " + prob_count + " issues";
        button.disabled = false;
        button.onclick = function(e) {
            const table = document.getElementById("modal-table");
            const colors = ["bg-info", "bg-success", "bg-warning", "bg-danger", "bg-light", "bg-primary"];
            for (var key in columnTypeCounts) {
                if (Object.keys(columnTypeCounts[key]).length > 1 || Object.keys(columnTypeCounts[key]).length == 0) {
                    let row = table.insertRow();
                    let cCount = 0;
                    let n = row.insertCell()
                    n.innerHTML = key;
                    let numIssues = row.insertCell();
                    numIssues.innerHTML = Object.keys(columnTypeCounts[key]).length;
                    let dtypes = document.createElement("div");
                    dtypes.classList.add("progress-stacked");
                    for (var d in columnTypeCounts[key]) {
                        let dt = document.createElement("div");
                        dt.classList.add("progress");
                        dt.role = "progressbar";
                        dt.ariaLabel = d;
                        dt.ariaValueMax = "100";
                        dt.ariaValue = "0";
                        dt.ariaValueNow = Math.round(100 - lines.length / columnTypeCounts[key][d]);
                        dt.style = "width: " + dt.ariaValueNow + "%" ;
                        let color = document.createElement("div");
                        color.classList.add("progress-bar", bg-colors[cCount], "text-dark", "progress-bar-striped", "progress-bar-animated");
                        color.innerText = d
                        cCount++;
                        if (cCount >= colors.length){
                            cCount = 0;
                        }
                        dt.appendChild(color);
                        dtypes.appendChild(dt);
                    }
                    dt_cell = row.insertCell();
                    dt_cell.innerHTML = dtypes.outerHTML;
                }
            }
        }
    }
    else {
        button.innerText = "No issues detected.";
        button.disabled = true;
    }
    corrections.appendChild(button);
    
}

function arrayParseValueCount(lines) {
    var columnTypeCount = {};
    var typeCounts = {};
    for (var i = 0; i < lines[0].length; i++) {
        for (var j = 1; j < lines.length; j++) {
            item = lines[j][i];
            let type;
            if (Number(item) != NaN && Number(item) == item) {
                if (item % 1 === 0) {
                    type = 'integer';
                }
                else {
                    type = 'float';
                }
            } else if (new Date(item) != 'Invalid Date' && !isNaN(new Date(item))) {
                type = 'datetime';
            } else if (item === 'NaN' || item === 'null' || item === 'None') {
                type = 'None';
            } else if (/^[0-9A-Fa-f]+$/.test(item)) {
                type = 'hexadecimal';
            } else {
                type = 'string';
            }
            if (typeCounts[type]) {
                typeCounts[type]++;
            } else {
                typeCounts[type] = 1;
            }
        };
        columnTypeCount[lines[0][i]] = typeCounts;
        typeCounts = {};
    }
    return columnTypeCount;
}

function arrayParseValueCountMax(columnTypeCount) {
    var max = 0;
    var m_key = "";
    for (var key in columnTypeCount) {
            if (columnTypeCount[key] > max) {
                max = columnTypeCount[key];
                m_key = key;
            }
        }
    return m_key;
}

input_element.addEventListener("change", fileHandler, false);
