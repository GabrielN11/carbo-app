import axios from 'axios';
import { loading } from '../../stores/loading-store';

const baseUrl = 'http://127.0.0.1:5000'

export async function apiGet<T>(url: string, sendToken?: boolean): Promise<T>{
  try{
    loading.update(() => true)
    const token = localStorage.getItem('usertoken')
    const headers = {
      'Content-Type': 'application/json',
      'Authorization': sendToken ? 'Bearer ' + token : undefined
    }

    const {data} = await axios.get<T>(baseUrl + url, {
      headers
    })

    if(Object.keys(data).includes('error')){
      throw data
    }

    return data
  }catch(e: any){
    throw new Error(e.response.data.error)
  }finally{
    loading.update(() => false)
  }
}

export async function apiPost<T, A>(url: string, model: A, sendToken?: boolean): Promise<T>{
  try{
    loading.update(() => true)
    const token = localStorage.getItem('usertoken')
    const headers = {
      'Authorization': sendToken ? token : undefined
    }

    const {data} = await axios.post<T>(baseUrl + url, model, {headers})

    if(Object.keys(data).includes('error')){
      throw data
    }

    return data

  }catch(e: any){
    throw new Error(e.response.data.error)
  }finally{
    loading.update(() => false)
  }
}

export async function apiPut<T, A>(url: string, model: A, sendToken?: boolean): Promise<T>{
  try{
    loading.update(() => true)
    const token = localStorage.getItem('usertoken')
    const headers = {
      'Authorization': sendToken ? token : undefined
    }

    const {data} = await axios.put<T>(baseUrl + url, model, {headers})

    if(Object.keys(data).includes('error')){
      throw data
    }

    return data

  }catch(e: any){
    throw new Error(e.response.data.error)
  }finally{
    loading.update(() => false)
  }
}

export async function apiDelete<T, A>(url: string, sendToken?: boolean): Promise<T>{
  try{
    loading.update(() => true)
    const token = localStorage.getItem('usertoken')
    const headers = {
      'Authorization': sendToken ? token : undefined
    }

    const {data} = await axios.delete<T>(baseUrl + url, {headers})

    if(Object.keys(data).includes('error')){
      throw data
    }

    return data

  }catch(e: any){
    throw new Error(e.response.data.error)
  }finally{
    loading.update(() => false)
  }
}