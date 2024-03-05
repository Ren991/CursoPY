import React from "react"

const ContactList = ({contacts}) =>{
    return (
        <>
            <div>
                <h2>Contacts</h2>
                <table>
                    <thead>
                        <tr>
                            <th>Nombre</th>
                            <th>Apellido</th>
                            <th>Email</th>
                            <th>Acciones</th>
                        </tr>
                    </thead>
                    <tbody>
                        {contacts.map((contact)=>(
                            <tr key={contact.id}>
                                <td>{contact.firstName}</td>
                                <td>{contact.lastName}</td>
                                <td>{contact.email}</td>
                                <td>
                                    <button>Modificar</button>
                                    <button>Eliminar</button>

                                </td>
                            </tr>
                        ))}
                    </tbody>
                </table>
            </div>
        </>
    )
}


export default ContactList