# Using JSON-LD

See also: [Part 4 of the tutorial](https://linkml.io/linkml/intro/tutorial04.html)

This how-to guide walks you through some of the basics of working with JSON-LD and LinkML

## About JSON-LD

[JSON-LD](https://json-ld.org/) is a way of working with JSON documents that are also RDF
documents. JSON-LD can provide a powerful bridge between
"developer-friendly" JSON serializations and Linked Data
frameworks.

Well-constructed JSON-LD can be easy to work with in "traditional"
software and data science environments, while retaining benefits of
RDF and a direct conversion to RDF. However, there are also pitfalls
to be aware of.

Two key concepts to be aware of that make JSON-LD work for you:

 * Contexts
 * Framing

A full description of these is outside the scope of this guide, but we
will provide some practical examples.

To get a sense of JSON-LD, we recommend exploring the [JSON-LD Playground](https://json-ld.org/playground/)

## JSON-LD Example

Consider a simple data graph containing two person objects, grouped into a 'container' object:

```turtle
@prefix schema: <http://schema.org/> .
@prefix personinfo: <https://w3id.org/linkml/examples/personinfo/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://orcid.org/1234> a schema:Person ;
    schema:name "Clark Kent" ;
    schema:telephone "555-555-5555" ;
    personinfo:age 33 .

<https://orcid.org/4567> a schema:Person ;
    schema:name "Lois Lane" ;
    personinfo:age 34 .

[] a personinfo:Container ;
    personinfo:persons <https://orcid.org/1234>,
        <https://orcid.org/4567> .
```

We can use a standard JSON-LD compliant tool (for example, Apache
Jena) or the JSON-LD playground
to convert this to JSON-LD, which may look something like this:


```json
{
  "@graph" : [ {
    "@id" : "_:b0",
    "@type" : "personinfo:Container",
    "persons" : [ "https://orcid.org/4567", "https://orcid.org/1234" ]
  }, {
    "@id" : "https://orcid.org/1234",
    "@type" : "schema:Person",
    "name" : "Clark Kent",
    "telephone" : "555-555-5555",
    "personinfo:age" : 33
  }, {
    "@id" : "https://orcid.org/4567",
    "@type" : "schema:Person",
    "name" : "Lois Lane",
    "personinfo:age" : 34
  } ],
  "@context" : {
    "age" : {
      "@id" : "https://w3id.org/linkml/examples/personinfo/age",
      "@type" : "http://www.w3.org/2001/XMLSchema#integer"
    },
    "telephone" : {
      "@id" : "http://schema.org/telephone"
    },
    "name" : {
      "@id" : "http://schema.org/name"
    },
    "persons" : {
      "@id" : "https://w3id.org/linkml/examples/personinfo/persons",
      "@type" : "@id"
    },
    "schema" : "http://schema.org/",
    "xsd" : "http://www.w3.org/2001/XMLSchema#",
    "personinfo" : "https://w3id.org/linkml/examples/personinfo/"
  }
}
```

Hurray! We have a JSON form of our RDF graph. Developers can work with this format using familiar JSON parsers, not requiring any special RDF libraries. It can be stored in a Mongo Database, it can be queried using jq, ....

Hold your horses! Before handing this JSON to our fellow developers, let's take a closer look.

First you will see fields such as:

 * `@id`
 * `@type`

This violates common idioms with JSON documents, where fields are usually 'key-friendly'. As well as being unusual-looking, this structure could actually hinder development and even break some tooling.

**Pitfall Warning**

A classic mistake is trying to declare slots with names like `@id` and `@type` in the corresponding LinkML schema.

E.g.

```yaml
slots:
  "@id":
    identifier: true
  "@type":
    range: ...
```

While this is possible, it's almost certainly NOT what you want.

Thankfully, we don't have to give such ugly JSON to our fellow developers. In fact there are multiple ways to represent the same RDF as a JSON-LD document. We can make our JSON much more idiomatic through the use of JSON-LD *contexts*.


### Context

Let's provide an initial context for our JSON-LD

```json
{
   "@context": {
      "ORCID": "https://orcid.org/",
      "linkml": "https://w3id.org/linkml/",
      "personinfo": "https://w3id.org/linkml/examples/personinfo/",
      "schema": "http://schema.org/",
      "@vocab": "https://w3id.org/linkml/examples/personinfo/",
      "persons": {
         "@type": "@id"
      },
      "age": {
         "@type": "xsd:integer"
      },
      "full_name": {
         "@id": "schema:name"
      },
      "type": "@type",
      "id": "@id",
      "phone": {
         "@id": "schema:telephone"
      },
      "Person": {
         "@id": "schema:Person"
      }
   }
}
```

Don't worry about authoring these contexts for now (in fact, as we will see later, these can be autogenerated from LinkML schemas).

Using the [JSON-LD playground](https://json-ld.org/playground/) we can make JSON that is approaching something more idiomatic:

```
{
  "@context": {
    "ORCID": "https://orcid.org/",
    "linkml": "https://w3id.org/linkml/",
    "personinfo": "https://w3id.org/linkml/examples/personinfo/",
    "schema": "http://schema.org/",
    "@vocab": "https://w3id.org/linkml/examples/personinfo/",
    "persons": {
      "@type": "@id"
    },
    "age": {
      "@type": "xsd:integer"
    },
    "full_name": {
      "@id": "schema:name"
    },
    "type": "@type",
    "id": "@id",
    "phone": {
      "@id": "schema:telephone"
    },
    "Person": {
      "@id": "schema:Person"
    }
  },
  "@graph": [
    {
      "id": "_:b0",
      "type": "Container",
      "persons": [
        "ORCID:4567",
        "ORCID:1234"
      ]
    },
    {
      "id": "ORCID:1234",
      "type": "Person",
      "full_name": "Clark Kent",
      "phone": "555-555-5555",
      "personinfo:age": 33
    },
    {
      "id": "ORCID:4567",
      "type": "Person",
      "full_name": "Lois Lane",
      "personinfo:age": 34
    }
  ]
}
```

Ignore the `@context` blob at the top for now - that can easily be masked or imported over the web. We now have a list of Person objects

A general tip with JSON-LD is to expose the *compacted* structure, not the *expanded* one.

## Coordinating JSON-Schema and JSON-LD Contexts

JSON-LD contexts and JSON-Schema provide distinct ways of describing your data,
with JSON-Schema providing the *structural* description of how your information is organized,
and contexts providing the *semantics* (or at least a loose semantics consisting of reuse of URIs).

Despite these distinct purposes there is a lot of overlap and many organizations
end up manually maintaining these and keeping them in sync.

There are also additional challenges in that there are frequently multiple ways to *frame*
the same RDF graphs, but this is hard to capture in JSON-Schema, so a schema will typically
cover a single framing - other frameworks like SHACL may be used for a frame-independent
representation of the RDF.

All of this and the pitfalls mentioned above lead to confusion in how "traditional" JSON
frameworks and JSON-LD/RDF should be coordinated.

## LinkML and JSON-LD

LinkML provides a single "polyglot" language for describing multiple aspects of your data.

One of the value propositions of LinkML is that it allows a single Source of Truth with compilation
to multiple representations using generators.

This means that your data modelers can maintain a single schema, and then derive:

- JSON-LD contexts
- JSON-Schema
- Anything else (e.g. SHACL shape schema) 

For example, a minimal schema might be:
  
```yaml
prefixes:
  schema: http://schema.org/
  ...
Person:
  description: A person (alive, dead, undead, or fictional).
  class_uri: schema:Person
  attributes:
    id:
      identifier: true
    name:
      slot_uri: schema:name
    age:
      range: integer
    telephone:
      slot_uri: schema:telephone
```

This describes *both* the structure of our data objects, *and* the meaning
of elements of the schema, by mapping to vocabularies like schema.org

You can use the linkml toolchain to *directly* convert objects from JSON/YAML
to and from RDF, e.g.

```bash
linkml-convert -s personinfo.yaml data.json -o data.ttl
```

You can also use the generator framework to generate a JSON-LD context that
can be used for *deferred* conversion using standard RDF toolchains:

```bash
gen-json-ld-context personinfo.yaml -o personinfo.context.jsonld
```