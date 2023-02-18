<script lang='ts'>
    import { goto } from "$app/navigation";
    import { page } from "$app/stores";
    import getUserById from "$lib/api/endpoints/user/user-get-by-id";
    import { toNumber } from "lodash-es";
    import { onMount } from "svelte";
    import FoodList from "../../../components/food-list/food-list.svelte";
    import UserProfileModel from "../../../models/user/user-profile-model";
    import { displayToast } from "../../../stores/toast-store";
    import { user } from "../../../stores/user-store";

    let id: number;

    let userProfile: UserProfileModel = new UserProfileModel();

    async function fetchUser(){
        try{
            const res = await getUserById(id)

            userProfile = res.data
        }catch(e: any){
            displayToast(e.message, '#dc3545', 4000)
            goto('/')
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
    <title>Carbo App - {userProfile.username}</title>
    <meta
        name="description"
        content={`Perfil de ${userProfile.username} no Carbo App - Aplicativo para consulta de valores de 
    carboidratos de alimentos`}
    />
</svelte:head>

<section>
    <h2>{userProfile.username}</h2>
    {#if userProfile.id > 0}
        <FoodList profile profileId={userProfile.id}/>
    {/if}
</section>

<style>
    section {
        width: 100%;
        display: flex;
        flex-direction: column;
        align-items: center;
        padding-top: 30px;
    }

</style>
