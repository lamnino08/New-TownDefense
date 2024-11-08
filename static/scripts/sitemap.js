$(document).ready(function() {
    const data = [
        { "id": "1", "parent": "#", "text": "Company", "icon": "fas fa-building" },
        { "id": "2", "parent": "1", "text": "HR Department", "icon": "fas fa-users" },
        { "id": "3", "parent": "1", "text": "IT Department", "icon": "fas fa-laptop" },
        { "id": "4", "parent": "2", "text": "Recruitment", "icon": "fas fa-user-plus" },
        { "id": "5", "parent": "2", "text": "Employee Relations", "icon": "fas fa-user-friends" }
    ];

    // Initialize JSTree with custom theme and checkbox plugin
    $('#departmentTree').jstree({
        'core': {
            'data': data,
            'themes': {
                'dots': true,  // Enable dots for each node
                'icons': true
            }
        },
        'plugins': ['wholerow', 'contextmenu'],
        'contextmenu': {
            'items': function(node) {
                return {
                    'Add': {
                        'label': 'Add Sub-Department/Role',
                        'action': function() {
                            $('#addDepartmentModal').modal('show');
                            $('#parentDepartment').val(node.id);
                        }
                    },
                    'Edit': {
                        'label': 'Edit',
                        'action': function() {
                            editDepartment(node);
                        }
                    },
                    'Delete': {
                        'label': 'Delete',
                        'action': function() {
                            if (confirm('Are you sure you want to delete ' + node.text + '?')) {
                                $('#departmentTree').jstree('delete_node', node);
                            }
                        }
                    }
                };
            }
        }
    });

    // Save Department/Role
    window.saveDepartment = function() {
        const departmentName = $('#departmentName').val();
        const departmentDescription = $('#departmentDescription').val();
        const parentDepartment = $('#parentDepartment').val();
        const newNode = {
            id: String(Math.floor(Math.random() * 1000) + 10),
            parent: parentDepartment || '#',
            text: departmentName,
            icon: "fas fa-folder"
        };
        $('#departmentTree').jstree('create_node', parentDepartment || '#', newNode, "last");
        $('#addDepartmentModal').modal('hide');
        $('#departmentForm')[0].reset();
    };

    // Edit Department/Role
    function editDepartment(node) {
        $('#departmentName').val(node.text);
        $('#parentDepartment').val(node.parent);
        $('#addDepartmentModal').modal('show');

        // When saving changes
        $('#saveChangesButton').off().on('click', function() {
            $('#departmentTree').jstree('rename_node', node, $('#departmentName').val());
            $('#addDepartmentModal').modal('hide');
            $('#departmentForm')[0].reset();
        });
    }
});
