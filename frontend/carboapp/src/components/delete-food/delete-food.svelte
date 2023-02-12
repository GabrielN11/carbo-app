<script lang="ts">
    import Dialog, { Title, Content, Actions } from '@smui/dialog';
    import Button, { Label } from '@smui/button';
    import { displayToast } from '../../stores/toast-store';
    import deleteFood from '$lib/api/endpoints/food/delete-food';
    import { goto } from '$app/navigation';
   
    export let open = false;
    export let name = '';
    export let id: number;
    export let closeDialog: () => void;

    async function handleDelete(){
        try{
            const res = await deleteFood(id)

            displayToast(res.message, '#28a745', 4000)
            open = false;
            goto('/')
        }catch(e: any){
            displayToast(e.message, '#dc3545', 4000)
        }
    }
  </script>

<Dialog
  bind:open
  aria-labelledby="simple-title"
  aria-describedby="simple-content"
  on:SMUIDialog:closed={closeDialog}
>
  <Title id="simple-title">Confirmar</Title>
  <Content id="simple-content">Tem certeza que deseja excluir {name}?</Content>
  <div class='actions'>
    <Button on:click={closeDialog}>
      <Label>Cancelar</Label>
    </Button>
    <Button on:click={handleDelete}>
      <Label>Excluir</Label>
    </Button>
  </div>
</Dialog> 

<style>
     .actions{
        display: flex;
        justify-content: flex-end;
        align-items: center;
        gap: 8px;
        padding: 8px;
    }
</style>