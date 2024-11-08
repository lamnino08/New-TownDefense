function fileterEmpleyee() {
    const searchName = document.getElementById('searchInput').value.trim(); 
    const filterDepartment = document.getElementById('filterDepartment').value; 
    const filterRole = document.getElementById('filterRole').value; 

    const apiUrl = `/admin/api/filter-staff?` + (searchName ? `&name=${searchName}` : '') + (filterDepartment ? `&department=${filterDepartment}` : '') + (filterRole ? `&role=${filterRole}` : '');

    axios.get(apiUrl)
    .then(response => {
        const data = response.data;
        const tableBody = document.getElementById('employeeTableBody');
        tableBody.innerHTML = ''; 

        // Check if no data was found
        if (data.length === 0) {
            tableBody.innerHTML = '<tr><td colspan="7" class="text-center">No employees found</td></tr>';
            return;
        }

        // Loop through each employee and create table rows
        data.forEach((employee, index) => {
            const row = `
                <tr id="employee-${employee.StaffID}">
                    <td>${index + 1}</td>
                    <td class="employee-name">${employee.Name}</td>
                    <td class="employee-role">${employee.Role.Name}</td>
                    <td class="employee-department">
                        <img src="${employee.Role.Department.Icon}" alt="${employee.Role.Department.Name}" class="department-icon" />
                        ${employee.Role.Department.Name}
                    </td>
                    <td class="employee-phone">${employee.PhoneNumber}</td>
                    <td>
                        <span class="badge rounded-pill px-2 py-1 text-small ${employee.Status ? 'bg-success text-white' : 'bg-danger text-white'} status-badge"
                            data-id="${employee.StaffID}" onclick="toggleStatus(this)">
                            ${employee.Status ? 'Active' : 'Blocked'}
                        </span>
                    </td>
                    <td>
                        <a class="action-icon" href="#" data-id="${employee.StaffID}" onclick="OnShowViewDetailAccount(this)">
                            <i class="bi bi-eye"></i>
                        </a>
                        <a class="action-icon" href="#" data-bs-toggle="modal" data-bs-target="#employeeEditModal"
                            data-id="${employee.StaffID}" onclick="OnShowEditAccount(this)">
                            <i class="bi bi-pencil-square"></i>
                        </a>
                        <a class="action-icon" href="#" data-bs-toggle="modal" data-bs-target="#deleteAccountModal"
                            data-id="${employee.StaffID}" data-name="${employee.Name}" onclick="OnShowDeleteAccount(this)">
                            <i class="bi bi-trash"></i>
                        </a>
                    </td>
                </tr>
            `;
            tableBody.innerHTML += row; 
        });
    })
    .catch(error => {
        console.error('Error fetching employees:', error);
    });
}

function submitCreateAccountForm() {
    const accountName = document.getElementById('accountName').value;
    const accountUserName = document.getElementById('accountUserName').value;
    const accountRole = document.getElementById('addEmployeeRole').value;
    const accountPhone = document.getElementById('accountPhone').value;
    const accountPassword = document.getElementById('accountPassword').value;
    
    // Validation (You can add more validation if needed)
    if (!accountName || !accountRole || !accountPassword || !accountUserName) {
        toastr.error('Please fill out all required fields.');
        return;
    }

    // Prepare data to send
    const data = {
        name: accountName,
        username: accountUserName,
        roleId: accountRole,
        phone: accountPhone,
        password: accountPassword
    };

    axios.post('/admin/api/add_staff/', data)
        .then(function (response) {
            toastr.success('Account created successfully!');

            var modal = bootstrap.Modal.getInstance(document.getElementById('addAccountModal'));
            modal.hide();

            document.getElementById('addAccountForm').reset();
        })
        .catch(function (error) {
            toastr.error('Failed to create account. Please try again.');
            console.error('Error creating account:', error);
        });
}

function updateRoleAddAccount() {
    const selectedRoleId = document.getElementById('addEmployeeRole').value; 

    axios.get(`/api/department/getDepartmentByRole/${selectedRoleId}`)
        .then(function (response) {
            const department = response.data;

            const departmentSelect = document.getElementById('addEmployeeDepartment'); 
            departmentSelect.disabled = false; 

            for (let i = 0; i < departmentSelect.options.length; i++) {
                if (departmentSelect.options[i].value == department.DepartmentID) {
                    departmentSelect.selectedIndex = i; 
                    break;
                }
            }
        })
        .catch(function (error) {
            console.error('Error fetching departments:', error);
        });
}

function OnShowViewDetailAccount(button) {
    const id = button.getAttribute('data-id');
    const url = `/admin/api/get-staff/${id}/`;

    axios.get(url)
        .then(response => {
            const data = response.data;

            if (data.status === 'success') {
                const staff = data.data;

                document.getElementById('employeeUserNameDetail').textContent = staff.Username;
                document.getElementById('employeeNameDetail').textContent = staff.Name;
                document.getElementById('employeeRoleDetail').textContent = staff.Role.Name;  
                document.getElementById('employeeDepartmentDetail').textContent = staff.Role.Department.Name;  
                document.getElementById('employeePhoneDetail').textContent = staff.PhoneNumber;
                document.getElementById('employeePasswordDetail').textContent = staff.Password;
                document.getElementById('editButtonOnDetailModal').setAttribute("data-id", staff.StaffID);
                var myModal = new bootstrap.Modal(document.getElementById('employeeDetailModal'));
                myModal.show();
            } else {
                toastr.error('Staff not found', 'Error');
            }
        })
        .catch(error => {
            toastr.error('An error occurred while fetching staff data.', 'Error');
        });
};

function OnShowEditAccount(button) {
    const id = button.getAttribute('data-id');
    const url = `/admin/api/get-staff/${id}/`;

    axios.get(url)
        .then(response => {
            const data = response.data;
            console.log(data.data);
            if (data.status === 'success') {
                const staff = data.data;

                document.getElementById('employeeUserNameEdit').value = staff.Username;
                document.getElementById('employeeNameEdit').value = staff.Name;
                document.getElementById('employeeRoleEdit').value = staff.Role.RoleID 
                document.getElementById('employeeDepartmentEdit').value = staff.Role.Department.DepartmentID; 
                document.getElementById('employeePhoneEdit').value = staff.PhoneNumber;
                document.getElementById('employeePasswordEdit').value = staff.Password;

                const saveButton = document.getElementById('saveEmployeeButton');
                saveButton.setAttribute('data-id', id);
            } else {
                toastr.error('Staff not found', 'Error');
            }
        })
        .catch(error => {
            toastr.error('An error occurred while fetching staff data.', 'Error');
        });
}


function updateDepartment() {
    const roleSelect = document.getElementById('employeeRoleEdit');
    const departmentSelect = document.getElementById('employeeDepartmentEdit');
    
    alert(roleSelect.selectedIndex);
    const selectedRole = roleSelect.options[roleSelect.selectedIndex];
    const departmentId = selectedRole.getAttribute('data-department');
    
    for (let i = 0; i < departmentSelect.options.length; i++) {
        if (departmentSelect.options[i].value === departmentId) {
            departmentSelect.selectedIndex = i;
            break;
        }
    }
};

function toggleStatus(element) {
    const staffId = element.getAttribute('data-id');
    const currentStatus = element.textContent.trim() === 'Active' ? true : false;  

    const url = `/admin/api/update-status-staff/${staffId}/`;  
    const data = { status: !currentStatus }; 

    axios.post(url, data, {
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken'),  
        }
    })
    .then(response => {
        if (response.data.status === 'success') {
            if (data.status) {
                element.textContent = 'Active';
                element.classList.remove('bg-danger');
                element.classList.add('bg-success');
            } else {
                element.textContent = 'Blocked';
                element.classList.remove('bg-success');
                element.classList.add('bg-danger');
            }
        } else {
            toastr.error('Failed to update status', 'Error');
        }
    })
    .catch(error => {
        console.error('Error:', error);
        toastr.error('An error occurred while updating status', 'Error');
    });
}

function togglePasswordVisibility() {
    const passwordField = document.getElementById('employeePasswordEdit');
    const passwordIcon = document.getElementById('passwordIcon');

    if (passwordField.type === 'password') {
        passwordField.type = 'text'; 
        passwordIcon.classList.remove('bi-eye-slash'); 
        passwordIcon.classList.add('bi-eye'); 
    } else {
        passwordField.type = 'password'; 
        passwordIcon.classList.remove('bi-eye'); 
        passwordIcon.classList.add('bi-eye-slash'); 
    }
}

function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
}

function confirmEditEmployee() {
    var myModal = new bootstrap.Modal(document.getElementById('confirmEditModal'));
    myModal.show();
}

function saveEmployeeDetails(button) {
    // Get the staff ID from the button's data-id attribute
    const staffId = button.getAttribute('data-id');

    // Get the form element and create a FormData object from it
    const form = document.getElementById('editEmployeeForm');
    const formData = new FormData(form);

    // Convert FormData to a plain JavaScript object
    const data = {};
    formData.forEach((value, key) => {
        data[key] = value;
    });

    // Send the updated data to the backend
    axios.post(`/admin/api/update-staff/${staffId}/`, data, {
        headers: {
            'Content-Type': 'application/json',  // Set content type to JSON
        }
    })
    .then(response => {
        if (response.data.success) {
            toastr.success('Employee details updated successfully!');

            const updatedStaff = response.data.data;  // Updated staff data returned from the backend

            // Find the row element using the staff ID
            const rowElement = document.getElementById('employee-' + staffId);

            // Update the content of the row with the updated staff data
            rowElement.querySelector('.employee-name').textContent = updatedStaff.Name;
            rowElement.querySelector('.employee-role').textContent = updatedStaff.Role.Name;
            rowElement.querySelector('.employee-department').textContent = updatedStaff.Role.Department.Icon + updatedStaff.Role.Department.Name;
            rowElement.querySelector('.employee-phone').textContent = updatedStaff.PhoneNumber;

            const statusBadge = rowElement.querySelector('.status-badge');
            if (updatedStaff.Status) {
                statusBadge.classList.remove('bg-danger');
                statusBadge.classList.add('bg-success');
                statusBadge.textContent = 'Active';
            } else {
                statusBadge.classList.remove('bg-success');
                statusBadge.classList.add('bg-danger');
                statusBadge.textContent = 'Blocked';
            }
        } else {
            toastr.error('Failed to update employee details.');
        }
    })
    .catch(error => {
        console.error('Error:', error);
        toastr.error('An error occurred while updating employee details.');
    });
}



let deleteStaffId = null;
function OnShowDeleteAccount(button) {
    const id = button.getAttribute('data-id'); 
    const name = button.getAttribute('data-name'); 

    document.getElementById('employeeNameDelete').textContent = name;

    deleteStaffId = id;

    var myModal = new bootstrap.Modal(document.getElementById('deleteAccountModal'));
    myModal.show();
}

function OnDeleteAccount() {
    if (!deleteStaffId) {
        toastr.error('No employee selected for deletion', 'Error');
        return;
    }

    const url = `/admin/api/delete-staff/${deleteStaffId}/`; 

    axios.delete(url)
        .then(response => {
            const data = response.data;

            if (data.status === 'success') {
                toastr.success('Employee deleted successfully', 'Success');
            } else {
                toastr.error('Failed to delete employee', 'Error');
            }

            location.reload();
        })
        .catch(error => {
            toastr.error('An error occurred while deleting the employee', 'Error');
        });
}

function LoadChart(type, date) {
    let titleText = '';

    date = document.getElementById('selectedDate').value; 

    document.getElementById('daily-btn').classList.remove('active');
    document.getElementById('weekly-btn').classList.remove('active');
    document.getElementById('monthly-btn').classList.remove('active');

    if (type === 'daily') {
        document.getElementById('daily-btn').classList.add('active');
        titleText = 'Total Revenue and Number of Customers per Day';
    } else if (type === 'weekly') {
        titleText = 'Total Revenue and Number of Customers per Week';
        document.getElementById('weekly-btn').classList.add('active');
    } else if (type === 'monthly') {
        document.getElementById('monthly-btn').classList.add('active');
        titleText = 'Total Revenue and Number of Customers per Month';
    } else {
        return;
    }

    const url = `/api/finance/chart?name=${type}` + (date ? `&date=${date}` : date); 
    axios.get(url)
        .then(response => {
            const data = response.data.result;
            
            if (!data || data.length === 0) {
                console.error('No data available.');
                return;
            }

            const revenueData = data.map(item => Math.round(item.TotalRevenue));
            const customerCountData = data.map(item => item.TotalCustomers);

            const dateData = data.map((item, index) => {
                const date = new Date(item.Date);
                
                if (type === 'daily') {
                    return date.toLocaleDateString('en-US', { month: 'short', day: 'numeric' });
                } else if (type === 'weekly') {
                    if (index === 0) {
                        return 'This Week';
                    } else {
                        return `${index} Week${index > 1 ? 's' : ''} Ago`;
                    }
                } else if (type === 'monthly') {
                    return date.toLocaleDateString('en-US', { year: 'numeric', month: 'short' });
                }
            });

            // Chart container
            const chartElement = document.querySelector("#salesAnalyticsChart");
            if (!chartElement) {
                console.error("Element #salesAnalyticsChart not found");
                return;
            }

            // Set chart options dynamically
            var options = {
                chart: {
                    height: 350,
                    type: 'line',
                    stacked: false
                },
                series: [
                    {
                        name: 'Total Revenue',
                        type: 'column',
                        data: revenueData
                    },
                    {
                        name: 'Customers',
                        type: 'line',
                        data: customerCountData
                    }
                ],
                xaxis: {
                    categories: dateData
                },
                yaxis: [
                    {
                        title: {
                            text: 'Revenue (in USD)'
                        },
                        labels: {
                            formatter: function(value) {
                                return '$' + Math.round(value).toLocaleString();
                            }
                        }
                    },
                    {
                        opposite: true,
                        title: {
                            text: 'Number of Customers'
                        }
                    }
                ],
                title: {
                    text: titleText,
                    align: 'center'
                },
                markers: {
                    size: 4
                },
                dataLabels: {
                    enabled: true,
                    enabledOnSeries: [1] 
                }
            };

            var chart = new ApexCharts(chartElement, options);
            chart.render();
        })
        .catch(error => {
            console.error('Error fetching panel content:', error);
        });
}
