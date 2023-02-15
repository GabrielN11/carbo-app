<script lang='ts'>
    import { page } from '$app/stores';
</script>

<section>
    <iconify-icon icon="tabler:mood-sad-dizzy" style="color: white;" width=50></iconify-icon>
    <h2>Ops! Algo deu errado.</h2>
    <p>{$page.error?.message || ''}</p>
</section>

<style>
    section{
        padding-top: 20px;
        display: flex;
        gap: 7px;
        flex-direction: column;
        align-items: center;
    }
</style>