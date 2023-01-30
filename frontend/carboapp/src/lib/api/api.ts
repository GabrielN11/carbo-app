import axios from 'axios';

export async function apiGet<T>(url: string, sendToken?: boolean): Promise<T>{
  try{
    const token = localStorage.getItem('usertoken')
    const headers = {
      'Content-Type': 'application/json',
      'Authorization': sendToken ? token : undefined
    }

    const {data} = await axios.get<T>(url, {
      headers
    })

    console.log(data)

    if(Object.keys(data).includes('error')){
      throw data
    }

    return data
  }catch(e: any){
    throw new Error(e.response.data.error)
  }
}

export async function apiPost<T, A>(url: string, model: A, sendToken?: boolean): Promise<T>{
  try{
    const token = localStorage.getItem('usertoken')
    const headers = {
      'Authorization': sendToken ? token : undefined
    }

    const {data} = await axios.post<T>(url, model, {headers})

    if(Object.keys(data).includes('error')){
      throw data
    }

    return data

  }catch(e: any){
    throw new Error(e.response.data.error)
  }
}

export async function apiPut<T, A>(url: string, model: A, sendToken?: boolean): Promise<T>{
  try{
    const token = localStorage.getItem('usertoken')
    const headers = {
      'Authorization': sendToken ? token : undefined
    }

    const {data} = await axios.put<T>(url, model, {headers})

    if(Object.keys(data).includes('error')){
      throw data
    }

    return data

  }catch(e: any){
    throw new Error(e.response.data.error)
  }
}

export async function apiDelete<T, A>(url: string, sendToken?: boolean): Promise<T>{
  try{
    const token = localStorage.getItem('usertoken')
    const headers = {
      'Authorization': sendToken ? token : undefined
    }

    const {data} = await axios.delete<T>(url, {headers})

    if(Object.keys(data).includes('error')){
      throw data
    }

    return data

  }catch(e: any){
    throw new Error(e.response.data.error)
  }
}