function getPanelOfAdmin(panel) {
    const url = `/admin/get-view?panel=${panel}`;
    axios.get(url)
        .then(response => {
            const panelContent = document.getElementById('panel_content');
            panelContent.innerHTML = response.data;
            init_sitemap();
        })
        .catch(error => {
            console.error('Error fetching panel content:', error);
        });
}
function init_sitemap() {
    const url = `/structure/api/structure`;

    axios.get(url)
        .then(response => {
            const data = transformToTree(response.data); 
            
            $('#departmentTree').jstree({
                'core': {
                    'data': data,
                    'themes': {
                        'dots': true,
                        'icons': true
                    }
                },
                'plugins': ['wholerow', 'contextmenu', 'dnd' ],
                'contextmenu': {
                    'items': function (node) {
                        return {
                            'Add': {
                                'label': 'Add Sub-Department/Role',
                                'action': function () {
                                    $('#addDepartmentModal').modal('show');
                                    $('#parentDepartment').val(node.id);
                                }
                            },
                            'Edit': {
                                'label': 'Edit',
                                'action': function () {
                                    editDepartment(node);
                                }
                            },
                            'Delete': {
                                'label': 'Delete',
                                'action': function () {
                                    if (confirm('Are you sure you want to delete ' + node.text + '?')) {
                                        $('#departmentTree').jstree('delete_node', node);
                                    }
                                }
                            }
                        };
                    }
                }
            });

            $('#departmentTree').on('select_node.jstree', function (e, data) {
                const node = data.node;
                NodeClick(node)
            });


        })
        .catch(error => {
            console.error('Error fetching panel content:', error);
        });
}

// Helper function to transform the API response into a tree structure
function transformToTree(departments) {
    let treeData = [];

    function processDepartment(department, parentId = "#") {
        const departmentNode = {
            id: `department_${department.department_id}`,
            parent: parentId,
            text: department.name,
            icon: department.icon || "fas fa-building" // Default icon
        };

        treeData.push(departmentNode);

        // Add roles within the department
        if (department.roles) {
            department.roles.forEach(role => {
                const roleNode = {
                    id: `role_${role.role_id}`,
                    parent: departmentNode.id,
                    text: role.name,
                    icon: "fas fa-user-shield" // Icon for roles
                };

                treeData.push(roleNode);

                // Add staff within the role
                if (role.staffs) {
                    role.staffs.forEach(staff => {
                        const staffNode = {
                            id: `staff_${staff.staff_id}`,
                            parent: roleNode.id,
                            text: staff.name,
                            icon: "fas fa-user" // Icon for staff
                        };
                        treeData.push(staffNode);
                    });
                }
            });
        }

        // Recursively process sub-departments
        if (department.sub_departments) {
            department.sub_departments.forEach(subDept => processDepartment(subDept, departmentNode.id));
        }
    }

    departments.forEach(department => processDepartment(department));

    return treeData;
}


function NodeClick(node) {
    console.log(node.id);

    const attribue = node.id.split('_');
    const url = `/structure/api/get-detail?name=${attribue[0]}&id=${attribue[1]}`;
    console.log(url)
    axios.get(url)
        .then(response => {
            console.log(response.data)
        })
        .catch(e => {

        })
}
