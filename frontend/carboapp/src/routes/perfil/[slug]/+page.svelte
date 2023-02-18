<script lang="ts">
    import { goto } from "$app/navigation";
    import { page } from "$app/stores";
    import getUserById from "$lib/api/endpoints/user/user-get-by-id";
    import { toNumber } from "lodash-es";
    import { onMount } from "svelte";
    import FoodList from "../../../components/food-list/food-list.svelte";
    import UserProfileModel from "../../../models/user/user-profile-model";
    import { displayToast } from "../../../stores/toast-store";
    import Tab, { Label } from "@smui/tab";
    import TabBar from "@smui/tab-bar";
    import { user } from "../../../stores/user-store";

    let id: number;

    let userProfile: UserProfileModel = new UserProfileModel();

    let active = "Publicações";

    async function fetchUser() {
        try {
            const res = await getUserById(id);

            userProfile = res.data;
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
    <h2>{userProfile.username}</h2>
    <div class='tabs'>
        <TabBar
        tabs={["Publicações", "Favoritos"]}
        let:tab
        bind:active
    >
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

    .tabs{
        width: 500px;
        margin-bottom: 20px;
    }

    * :global(.mdc-tab-indicator .mdc-tab-indicator__content--underline) {
        border-color: var(--mdc-theme-secondary, #fff)
    }

    * :global(.mdc-tab__text-label) {
        color: var(--mdc-theme-secondary, #fff)
    }

    @media (max-width: 600px){
        .tabs{
            width: 300px;
        }
    }
</style>
