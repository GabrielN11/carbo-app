<script lang='ts'>
    import { goto } from "$app/navigation";
    import { page } from "$app/stores";
    import getUserById from "$lib/api/endpoints/user/user-get-by-id";
    import { toNumber } from "lodash-es";
    import { onMount } from "svelte";
    import UserModel from "../../../models/user/user-model";
    import { displayToast } from "../../../stores/toast-store";
    import { user } from "../../../stores/user-store";

    let id: number;

    let userProfile: UserModel = new UserModel();

    async function fetchUser(){
        try{
            const res = await getUserById(id)

            userProfile = res.data
        }catch(e: any){
            displayToast(e.message, '#dc3545', 4000)
        }
    }

    onMount(() => {
        try{
            id = toNumber($page.url.pathname.split('/')[2])

            if(isNaN(id)) throw new Error()

            fetchUser();
        }catch(e: any){
            goto('/')
        }
    })
</script>

<svelte:head>
    <title>Carbo App - Validação</title>
    <meta
        name="description"
        content="Validar conta no Carbo App - Aplicativo para consulta de valores de 
    carboidratos de alimentos"
    />
</svelte:head>

<section>

</section>

<style>

</style>
