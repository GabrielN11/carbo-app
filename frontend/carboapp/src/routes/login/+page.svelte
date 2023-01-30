<script lang='ts'>
	import welcome from '$lib/images/svelte-welcome.webp';
	import welcome_fallback from '$lib/images/svelte-welcome.png';
    import Textfield from '@smui/textfield';

    let username: string = '';
</script>

<svelte:head>
	<title>Carbo App - Entrar</title>
	<meta name="description" content="Login no Carbo App - Aplicativo para consulta de valores de 
    carboidratos de alimentos" />
</svelte:head>

<section>
	<form>
        <Textfield variant='filled' label='Usuário' bind:value={username} color='secondary'>

        </Textfield>

        <pre>{username}</pre>
    </form>
</section>

<style>

</style>
