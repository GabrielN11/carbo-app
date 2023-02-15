<script>
	import welcome from '$lib/images/svelte-welcome.webp';
	import welcome_fallback from '$lib/images/svelte-welcome.png';
	import Tooltip, { Wrapper } from '@smui/tooltip';
	import Fab, { Icon } from '@smui/fab';
    import AddFood from '../components/add-food/add-food.svelte';
    import { user } from '../stores/user-store';
    import FoodList from '../components/food-list/food-list.svelte';

	let openDialog = false;
</script>

<svelte:head>
	<title>Carbo App</title>
	<meta name="description" content="Svelte demo app" />
</svelte:head>

<section>
	<FoodList/>
	{#if $user}
	<AddFood open={openDialog} closeHandler={() => {
		openDialog = false
	}} id={undefined}/>
	<div class='fab-button'>
		<Wrapper>
			<Fab on:click={() => {
				openDialog = true
			}}>
				<iconify-icon icon="material-symbols:add" style="color: #46254f;" width="40" height="40"></iconify-icon>
			</Fab>
			<Tooltip>Adicionar Alimento.</Tooltip>
		  </Wrapper>
	</div>
	{/if}
</section>

<style>
	.fab-button{
		position: fixed;
		bottom: 20px;
		right: 20px;
	}
</style>
