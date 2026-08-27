   function edit(id,todo,todo_dis)
    {
        console.log(id);
        console.log(todo);
        console.log(todo_dis);

        $('#edit_id').val(id);
        $('#edit_todo').val(todo);
        $('#edit_todo_dis').val(todo_dis);
        $('#editModal').modal("show");
    }

    $('#editTodoForm').submit(function(e){
        e.preventDefault();

        let id=$('#edit_id').val();
        let data= $(this).serialize();

        $.ajax({
            url: `/edit/${id}/`,
            type:"POST",
            data:data,
            success:function(res){
               $('#editModal').modal("hide"); 
               location.reload();   
            }
        })
    });
        
    