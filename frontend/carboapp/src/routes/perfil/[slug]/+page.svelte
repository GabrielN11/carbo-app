<script lang="ts">
    import { goto } from "$app/navigation";
    import { page } from "$app/stores";
    import getUserById from "$lib/api/endpoints/user/user-get-by-id";
    import { isEmpty, toNumber } from "lodash-es";
    import { onMount } from "svelte";
    import FoodList from "../../../components/food-list/food-list.svelte";
    import UserProfileModel from "../../../models/user/user-profile-model";
    import { displayToast } from "../../../stores/toast-store";
    import Tab, { Label } from "@smui/tab";
    import TabBar from "@smui/tab-bar";
    import IconButton from "@smui/icon-button";
    import Tooltip, { Wrapper } from "@smui/tooltip";
    import Textfield from "@smui/textfield";
    import { user } from "../../../stores/user-store";
    import alterUsername from "$lib/api/endpoints/user/user-put";
    import UserPutModel from "../../../models/user/user-put-model";

    let id: number;

    let edit: boolean = false;
    let username: string = ''
    let error: boolean = false;

    let userProfile: UserProfileModel = new UserProfileModel();

    let active = "Publicações";

    async function handleSubmit(e: SubmitEvent){
        e.preventDefault()

        if(isEmpty(username)){
            error = true
            return
        }

        error = false

        try{
            const res = await alterUsername(userProfile.id, new UserPutModel(username))

            displayToast(res.message, '#28a745', 4000)

            userProfile.username = username
            edit = false
        }catch(e: any){
            displayToast(e.message, "#dc3545", 4000);
        }
    }

    async function fetchUser() {
        try {
            const res = await getUserById(id);

            userProfile = res.data;
            username = res.data.username;
        } catch (e: any) {
            displayToast(e.message, "#dc3545", 4000);
            goto("/");
        }
    }

    onMount(() => {
        try {
            id = toNumber($page.url.pathname.split("/")[2]);

            if (isNaN(id)) throw new Error();

            fetchUser();
        } catch (e: any) {
            goto("/");
        }
    });
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
    <div class="profile-title">
        {#if !edit}
            <h2>{userProfile.username}</h2>
            {#if $user && $user.id === userProfile.id}
                <Wrapper>
                    <IconButton on:click={() => (edit = true)}
                        ><iconify-icon
                            icon="material-symbols:edit"
                            style="color: white;"
                        />
                    </IconButton>
                    <Tooltip>Editar nome de usuário</Tooltip>
                </Wrapper>
            {/if}
        {:else}
        <form class='profile-title' on:submit={handleSubmit}>
            <Textfield
                style='width: 100%'
                variant="filled"
                label="Nome de Usuário"
                invalid={error}
                bind:value={username}
                color="secondary"
            >
            </Textfield>
            <Wrapper>
                <IconButton type='submit'>
                    <iconify-icon icon="material-symbols:save-as" style="color: white;"></iconify-icon>
                </IconButton>
                <Tooltip>Salvar</Tooltip>
            </Wrapper>
            <Wrapper>
                <IconButton on:click={() => (edit = false)}>
                    <iconify-icon icon="material-symbols:cancel-outline" style="color: white;"></iconify-icon>
                </IconButton>
                <Tooltip>Cancelar</Tooltip>
            </Wrapper>
        </form>
        {/if}
    </div>
    <div class="tabs">
        <TabBar tabs={["Publicações", "Favoritos"]} let:tab bind:active>
            <Tab {tab}>
                <Label>{tab}</Label>
            </Tab>
        </TabBar>
    </div>
    {#if active === "Publicações"}
        <p>Alimentos publicados por este usuário:</p>
        {#if userProfile.id > 0}
            <FoodList profile profileId={userProfile.id} />
        {/if}
    {:else}
        <p>Alimentos favoritados por este usuário:</p>
        {#if userProfile.id > 0}
            <FoodList favorite profileId={userProfile.id} />
        {/if}
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

    .tabs {
        width: 500px;
        margin-bottom: 20px;
    }

    * :global(.mdc-tab-indicator .mdc-tab-indicator__content--underline) {
        border-color: var(--mdc-theme-secondary, #fff);
    }

    * :global(.mdc-tab__text-label) {
        color: var(--mdc-theme-secondary, #fff);
    }

    .profile-title {
        display: flex;
        gap: 7px;
        align-items: center;
    }

    form{
        margin-bottom: 2rem;
    }

    @media (max-width: 600px) {
        .tabs {
            width: 300px;
        }
    }
</style>
