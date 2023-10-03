# Custom GPT Code Completion

## Model
- [Link](https://huggingface.co/codellama/CodeLlama-13b-Instruct-hf)
- [Space](https://huggingface.co/spaces/codellama/codellama-13b-chat)
- created by Meta

## Prompt

```
Write a charming short story in markdown using json for code samples. The story has to be provided as JSON in the markdown (and wrap the json with "```json" for markdown syntax highlighting), adhering to the IDocument interface below:

export interface IDocument {
/** id: the unique identifier of the Document /
id: string | number;
/* name: the name of the document /
name: string;
/* sections: the various sections the document has /
sections?: Section[];
/* sectionCount: the number of sections when the document gets returned in a list /
sectionCount?: number;
/* templateId?: the optional template from which the document was created*/
templateId?: string | number;
/** collectionId?: the optional collection the document belongs to /
collectionId?: string | number;
/* userPrompt?: */
userPrompt?: string;
}

export interface Section {
name: string;
type: 'Text' | 'Image' | 'Audio' | 'Video';
data: any;
displayOrder: number;
children?: Section[];
}
```