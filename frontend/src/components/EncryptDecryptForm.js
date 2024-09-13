import React, { useState, useEffect } from 'react';
import './EncryptDecryptForm.css';

function EncryptDecryptForm() {
    const [file, setFile] = useState(null);
    const [text, setText] = useState('');
    const [password, setPassword] = useState('');
    const [dictionary, setDictionary] = useState('');
    const [result, setResult] = useState('');
    const [foundPassword, setFoundPassword] = useState('');
    const [decryptedText, setDecryptedText] = useState('');
    const [mode, setMode] = useState('encrypt');
    const [inputType, setInputType] = useState('text');
    const [encryptionType, setEncryptionType] = useState('password'); // State for selecting encryption type

    // Clear text fields when mode changes
    useEffect(() => {
        setText('');
        setPassword('');
        setDictionary('');
        setResult('');
        setFoundPassword('');
        setDecryptedText('');
    }, [mode, encryptionType, inputType]);

    const handleFileChange = (e) => {
        const fileReader = new FileReader();
        fileReader.onload = (event) => {
            setText(event.target.result);
        };
        fileReader.readAsText(e.target.files[0]);
        setFile(e.target.files[0]);
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        let url = '';
        let body = { text };

        if (mode === 'encrypt' || mode === 'decrypt') {
            url = mode === 'encrypt' ? '/encrypt' : '/decrypt';
            if (encryptionType === 'password') {
                body.password = password;
            } else if (encryptionType === 'dictionary') {
                body.dictionary = JSON.parse(dictionary);
            }
        } else {
            url = '/find_password';
        }

        const response = await fetch(`http://localhost:5000${url}`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(body),
        });

        const data = await response.json();
        
        if (mode === 'find_password') {
            setFoundPassword(data.password);
            setDecryptedText(data.decrypted_text);
        } else {
            setResult(data.encrypted_text || data.decrypted_text);
        }
    };

    return (
        <div className="form-container">
            <h1>Vigenère Cipher Web Application</h1>
            <form onSubmit={handleSubmit}>
                <div className="input-type-selection">
                    <label>
                        <input
                            type="radio"
                            value="text"
                            checked={inputType === 'text'}
                            onChange={() => setInputType('text')}
                        />
                        Enter Text
                    </label>
                    <label>
                        <input
                            type="radio"
                            value="file"
                            checked={inputType === 'file'}
                            onChange={() => setInputType('file')}
                        />
                        Upload File
                    </label>
                </div>

                {inputType === 'text' ? (
                    <textarea
                        rows="5"
                        value={text}
                        onChange={(e) => setText(e.target.value)}
                        placeholder="Enter text here"
                    />
                ) : (
                    <div className="file-input">
                        <label htmlFor="file-upload">Upload Text File:</label>
                        <input type="file" id="file-upload" onChange={handleFileChange} />
                    </div>
                )}

                <div className="encryption-type-selection">
                    <label>
                        <input
                            type="radio"
                            value="password"
                            checked={encryptionType === 'password'}
                            onChange={() => setEncryptionType('password')}
                        />
                        Use Password
                    </label>
                    <label>
                        <input
                            type="radio"
                            value="dictionary"
                            checked={encryptionType === 'dictionary'}
                            onChange={() => setEncryptionType('dictionary')}
                        />
                        Use Dictionary
                    </label>
                </div>

                {encryptionType === 'password' && (
                    <input
                        type="text"
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                        placeholder="Enter password"
                    />
                )}

                {encryptionType === 'dictionary' && (
                    <textarea
                        rows="5"
                        value={dictionary}
                        onChange={(e) => setDictionary(e.target.value)}
                        placeholder='Enter dictionary as JSON, e.g., {"a": "b", "b": "c", ...}'
                    />
                )}

                <div className="options">
                    <select value={mode} onChange={(e) => setMode(e.target.value)}>
                        <option value="encrypt">Encrypt</option>
                        <option value="decrypt">Decrypt</option>
                        <option value="find_password">Find Password</option>
                    </select>
                </div>

                <br />
                <button type="submit">Submit</button>
            </form>

            {mode === 'find_password' ? (
                <>
                    <h2>Found Password</h2>
                    <textarea rows="1" value={foundPassword} readOnly />

                    <h2>Decrypted Text</h2>
                    <textarea rows="5" value={decryptedText} readOnly />
                </>
            ) : (
                <>
                    <h2>Result</h2>
                    <textarea rows="5" value={result} readOnly />
                </>
            )}
        </div>
    );
}

export default EncryptDecryptForm;
