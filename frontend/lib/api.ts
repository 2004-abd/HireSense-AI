export const API_URL = process.env.NEXT_PUBLIC_API_URL || "http://127.0.0.1:8000";
export function getToken(){if(typeof window==="undefined")return null;return localStorage.getItem("token");}
export function getUserName(){if(typeof window==="undefined")return "";return localStorage.getItem("userName")||"";}
export function saveAuth(token:string,userName:string,email:string){localStorage.setItem("token",token);localStorage.setItem("userName",userName);localStorage.setItem("email",email);}
export function logout(){localStorage.removeItem("token");localStorage.removeItem("userName");localStorage.removeItem("email");window.location.href="/login";}
export function getErrorMessage(data:any,fallback="Something went wrong."){if(typeof data?.detail==="string")return data.detail;if(Array.isArray(data?.detail))return data.detail.map((err:any)=>err.msg||JSON.stringify(err)).join(", ");if(data?.message)return data.message;return fallback;}
