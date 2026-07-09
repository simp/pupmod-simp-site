# AGENTS.md

This file provides guidance to AI agents when working with code in this repository.

## What this module does

`simp-site` is a **deliberately empty** SIMP Puppet module. It ships no classes,
defines, functions, types, facts, or templates — the README says so on its own
line: "This module is empty on purpose, and is intended to contain site-specific
classes." (`README.md:20`).

Its purpose is to give a SIMP deployment a **blessed, pre-created home for
site-local Puppet code**. SIMP ships `simp-site` so that site-specific classes
(e.g. `site::my_thing`) have a module namespace that already exists, is on the
Forge, and comes with the full SIMP test/CI/release scaffolding in place — so
the first bit of local code you add is immediately lintable, testable, and
buildable without standing up a new module from scratch.

Because there is no code yet, there is nothing to configure and nothing to
apply. The value of the module today is entirely the scaffolding: `metadata.json`,
the `Gemfile`, the `spec/` harness, and the GitHub Actions workflow that are all
ready for the moment someone drops a class into `manifests/`.

### Gotchas / non-obvious details

- **There is genuinely no manifest.** `manifests/`, `lib/`, and `templates/`
  contain only a `0`-byte `.gitkeep` placeholder each — nothing else. Adding
  functionality means creating a new `.pp` file under `manifests/` (e.g.
  `manifests/init.pp` for `class site`, or `manifests/foo.pp` for `site::foo`).
  Do not go looking for existing business logic; there is none.
- **The unit spec is a placeholder, not a real test.** `spec/classes/site_spec.rb`
  prints an ASCII whale and asserts `expect(true).to be_truthy` for every
  supported OS. It exists so `rake spec` has something to run, not to verify
  behavior. When you add a real class, replace/extend this with an actual
  rspec-puppet test.
- **There is NO `simp_options` / `simplib::lookup` seam.** Unlike most SIMP
  modules, this one consumes nothing from `simp_options::*` — there is no code to
  route toggles through. `simp/simplib` is a declared dependency for consistency
  and future use, not because anything calls it yet.
- **The supported-OS matrix in `metadata.json` is stale.** It lists only
  CentOS 6/7, RedHat 6/7, and OracleLinux 6/7 (`metadata.json:33-56`) — there is
  no EL8/9/10 entry. This is genuinely old baseline metadata; do not treat the
  EL6/7 list as a current statement of support. If you add code with real OS
  constraints, refresh this matrix.
- **The Puppet requirement is an old baseline too.** `puppet >= 7.0.0 < 9.0.0`
  (`metadata.json:60-64`) and the `Gemfile` default `['>= 7', '< 9']`
  (`Gemfile:23`) predate SIMP's Puppet → OpenVox migration. When the baseline
  moves this module to `openvox`, update these to match.

## Dependencies

Module dependencies (from `metadata.json:12-23`):

- `simp/simplib` `>= 4.9.0 < 5.0.0` — declared for consistency with the SIMP
  module family; nothing in this (empty) module calls it yet.
- `puppetlabs/stdlib` `>= 8.0.0 < 10.0.0` — same: declared, currently unused.

There are **no optional dependencies** (no `simp.optional_dependencies` block in
`metadata.json`).

Runtime requirement (from `metadata.json:57-64`): `puppet >= 7.0.0 < 9.0.0`.
This is an old baseline; SIMP is migrating Puppet → OpenVox, so when
`metadata.json` switches this to `openvox`, update this line to match.

Supported OS matrix (from `metadata.json:24-56`): CentOS 6/7; RedHat 6/7;
OracleLinux 6/7 — stale (see gotchas above).

## Repository layout

- `manifests/`, `lib/`, `templates/` — each contains only a `0`-byte `.gitkeep`
  placeholder. These are the empty homes for future classes, Ruby
  facts/functions/types, and templates respectively.
- `metadata.json` — name (`simp-site`), version (`2.2.0`), dependencies, the
  (stale) OS matrix, and the Puppet requirement.
- `README.md` — SIMP boilerplate plus the "empty on purpose" statement
  (`README.md:20`).
- `spec/classes/site_spec.rb` — placeholder unit test (ASCII whale +
  `expect(true).to be_truthy`); not a real behavioral test.
- `spec/spec_helper.rb` — standard SIMP rspec harness; requires
  `puppetlabs_spec_helper/module_spec_helper` (`spec/spec_helper.rb:11`).
  Carries a **puppetsync** notice (baseline-managed).
- `Gemfile` — baseline-managed gem pins; also carries a **puppetsync** notice.
- `.github/workflows/pr_tests.yml` — CI (see below).
- No `data/`, `hiera.yaml`, `types/`, `REFERENCE.md`, or acceptance suite — none
  are needed while the module is empty.

**CI (`.github/workflows/pr_tests.yml`):** the standard six SIMP jobs only —
`puppet-syntax`, `puppet-style`, `ruby-style`, `file-checks`, `releng-checks`,
and `spec-tests`. **There is NO acceptance job**, and there is **no
`spec/acceptance/nodesets/` directory** (0 nodesets) — appropriate for a module
with no code to exercise. The workflow pins `PUPPET_VERSION: '~> 7'`.

## Common commands

```sh
# Install dependencies
bundle install

# Run the (placeholder) unit tests
bundle exec rake spec

# Puppet lint
bundle exec rake lint

# Ruby lint
bundle exec rake rubocop
```

Relevant gem pins (from `Gemfile`): `rubocop ~> 1.88.0` (`Gemfile:16`),
`puppetlabs_spec_helper ~> 8.0.0` (`Gemfile:30`), `simp-rake-helpers ~> 5.24.0`
(`Gemfile:36`), `simp-beaker-helpers ~> 2.0.0` (`Gemfile:52`). The only Puppet
implementation gem pulled in is the **`puppet` gem** via
`gem 'puppet', puppet_version` (`Gemfile:29`), with `puppet_version` defaulting
to `['>= 7', '< 9']` (`Gemfile:23`).

## Conventions

- **Keep it honest and empty until it isn't.** Do not add speculative classes,
  a `simp_options` seam, or fixture scaffolding "just in case." Add exactly the
  code a site actually needs, then add the matching test and (if warranted)
  update `metadata.json`.
- **When you add your first class,** replace the placeholder
  `spec/classes/site_spec.rb` with a real rspec-puppet test, and refresh the
  stale OS matrix and Puppet requirement in `metadata.json` if the new code has
  real constraints.
- **`Gemfile` and `spec/spec_helper.rb` carry a puppetsync notice** — they are
  baseline-managed and the next sync overwrites local edits. Push changes to
  those files upstream to the SIMP baseline, not here.
- **Match SIMP Puppet style** for any code you add: 2-space indentation and
  aligned-arrow parameter/attribute style, consistent with the rest of the SIMP
  module family.
