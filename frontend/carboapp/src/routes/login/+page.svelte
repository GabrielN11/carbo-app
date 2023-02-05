<script lang="ts">
    import welcome from "$lib/images/svelte-welcome.webp";
    import welcome_fallback from "$lib/images/svelte-welcome.png";
    import Textfield from "@smui/textfield";
    import Loading from "../../components/loading/loading.svelte";
    import Button, { Label } from "@smui/button";
    import { isEmpty } from "lodash-es";
    import signIn from "$lib/api/endpoints/auth/login";
    import UserLoginModel from "../../models/user/user-login-model";
    import { setContext, getContext } from "svelte";
    import { redirect } from "@sveltejs/kit";
    import ToastModel from "../../models/toast/toast-model";
    import Toast from "../../components/toast/toast.svelte";
    import { onMount } from 'svelte';


    let username: string = "";
    let password: string = "";

    let error: boolean[] = [false, false];
    let toasts: ToastModel[] = [];

    function displayToast(message: string, color: string){
        const toastItem = new ToastModel(color, 2000, message);

        toasts = [toastItem, ...toasts]
        
        setTimeout(() => {            
            const last = toasts.length - 1
            toasts = toasts.filter((_, index) => index !== last)
        }, 2000)
    }

    function validateField(index: number) {
        if(index === 0){
            if(isEmpty(username)){
                error[0] = true
            }else{
                error[0] = false
            }
        }else{
            if(isEmpty(password)){
                error[1] = true
            }else{
                error[1] = false
            }
        }
    }

    function load(){
        redirect(302, '/')
    }


    async function onSubmit(e: SubmitEvent) {
        e.preventDefault();

        validateField(0);

        validateField(1);

        if (error.includes(true)) return;

        try{
            const res = await signIn(new UserLoginModel(username, password))

            localStorage.setItem('usertoken', res.data.token)

        }catch(e: any){
            displayToast(e.message, '#ff0000')
        }

        
    }
</script>

<svelte:head>
    <title>Carbo App - Entrar</title>
    <meta
        name="description"
        content="Login no Carbo App - Aplicativo para consulta de valores de 
    carboidratos de alimentos"
    />
</svelte:head>

<section>
    <form on:submit={onSubmit}>
        <h2>Login</h2>
        <p>Entre para poder salvar os carboidratos de seus alimentos!</p>
        <fieldset>
            <Textfield
                style='width: 100%'
                variant="filled"
                label="Usuário"
                invalid={error[0]}
                bind:value={username}
                color="secondary"
                on:change={() => validateField(0)}
            >
            </Textfield>
        </fieldset>
        <fieldset>
            <Textfield
                style='width: 100%'
                variant="filled"
                label="Senha"
                type='password'
                invalid={error[1]}
                bind:value={password}
                color="secondary"
                on:change={() => validateField(1)}
            >
            </Textfield>
        </fieldset>
        <fieldset>
            <Button touch variant="outlined" color="secondary" type="submit" style='width: 100%'>
                <Label>Entrar</Label>
            </Button>
        </fieldset>
    </form>
    <Toast toast={toasts}/>
</section>

<style>
    p {
        padding: 0 5px;
        text-align: center;
    }
    form {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        width: 100%;
        padding-top: 75px;
    }

    fieldset {
        width: 254px;
        border: none;
    }

    @media(min-width: 600px){
        fieldset{
            width: 400px;
        }
    }
</style>
